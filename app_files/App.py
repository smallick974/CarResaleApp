'''
Created on 19-Feb-2022

@author: Srijan-PC
'''
from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from flask_session import Session
from Users import Users
from Cars import Cars
from ResetPassword import ResetPassword
import os
from werkzeug.utils import secure_filename
import DbConUtil
from urllib.request import urlopen
import json

app= Flask(__name__)
app.secret_key = "56TiQWdoVayEhqJQezBb4n3k5QlnPIxjpfx"

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

def validateFileType(filename):
    image_folder,file_extensions = DbConUtil.getFileConfig()
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in file_extensions


@app.route('/')
def homepage():
    return render_template("Home.html")

@app.route('/nav', methods=['POST','GET'])
def nav():
    return render_template("Nav_Bar.html")

@app.route('/Home', methods=['POST','GET'])
def usersignup():
    usersignupdet = Users().userSignUp(request.form)
    if 'ERROR' in usersignupdet:
        return jsonify(usersignupdet)
    else:
        usercred = Users().userLogin(request.form)
        session["userData"] = usercred
        return jsonify(url_for('homepage'))

@app.route('/Welcome', methods =['POST','GET'])
def signin(): 
    if request.method == "POST":
        usercred = Users().userLogin(request.form)
        if 'Error' in usercred:
            return jsonify(usercred)
        else:    
            session["userData"] = usercred
            return jsonify(url_for('homepage'))           

@app.route('/Logout',methods =['POST','GET'])
def logout():
    session.pop("userData",None)
    return redirect(url_for('homepage'))   
    
@app.route('/Profile', methods=['POST','GET'])
def displayprofile():
    data=Users().displayProfile(session["userData"][0][1],None)
    return render_template("Profile.html",profiledata=data)

@app.route('/SellerDetails/<userid>', methods=['GET'])
def getSellerDetails(userid):
    sellerdata=Users().displayProfile(None,userid)
    return jsonify(sellerdata)

@app.route('/ProfileUpdate', methods=['POST','GET'])
def updateprofile():
    if request.method == "POST":
        userId = ''
        if "userId" in request.form:
            userId = request.form.get('userId')
        else:
            userId = session["userData"][0][3]
        updateprofile = Users().userUpdate(request.form,userId,None)
        if 'ERROR' in updateprofile:
            return jsonify(updateprofile)
        elif userId == session["userData"][0][3]:
            return jsonify(url_for('displayprofile'))
        else:
            return jsonify(url_for('admin'))

@app.route('/ResetPassword', methods=['POST','GET'])
def resetpassword():
    otp = ResetPassword().generateOTP()
    user_emailid = request.args.get('user_emailid', type=str)
    result = ResetPassword().sendEmail(user_emailid,otp)
    if result == 'SUCCESS':     
        return jsonify(otp=otp)
    else:
        return jsonify(result)                
    
@app.route('/NewCar', methods=['POST','GET'])
def newcar():
    car_manufacturer = list(Cars().getCarManufacturer('true',''))
    print(Cars().getCarManufacturer('true',''))
    print(car_manufacturer)
    return render_template("UploadCar.html",car_manufacturer_list=car_manufacturer)    

@app.route('/Search', methods=['POST','GET'])
def searchdata():
    form_value = request.args.get('value', type=str)
    isactive = request.args.get('isactive')
    car_models = Cars().getCarModels(form_value,isactive)
    return jsonify(selected_car_models=car_models) 

@app.route('/CarDetails', methods=['POST','GET'])
def GetCarDetails():
    manufacturer = request.args.get('lstmanufacture', type=str)
    model = request.args.get('lstmodel', type=str)
    year = request.args.get('lstyear', type=str)
    condition = request.args.get('lstcondition', type=str)
    cylinder = request.args.get('lstcylinder', type=str)
    fueltype = request.args.get('lstfueltype', type=str)
    drivetype = request.args.get('lstdrivetype', type=str)
    state = request.args.get('lststate', type=str)
    size = request.args.get('lstsize', type=str)
    searchText = request.args.get('searchText', type=str)
    minprice = request.args.get('minprice',type=str)
    maxprice = request.args.get('maxprice',type=str)
    wishlisted_cars = {}
    cars = Cars().getCars(None,manufacturer,model,year,condition,cylinder,fueltype,drivetype,state,size,searchText,minprice,maxprice)
    uniquecardetails = Cars().getUniqueCar(cars)
    if(session.__contains__("userData")):
        wishlisted_cars = Cars().getWishlistedCars(session["userData"][0][3])
    return jsonify(car_list=uniquecardetails, wishlisted_cars=wishlisted_cars,sessionvar = session) 

@app.route('/UpdateCar/<carid>', methods=["POST","GET"])
def updateCar(carid):
    if request.method == 'GET':
        carimages = Cars().getCarImages(carid)
        car_manufacturer = list(Cars().getCarManufacturer('true',''))
        cardetails = Cars().getCars(carid,None,None,None,None,None,None,None,None,None,None,None,None)
        carmodels = Cars().getCarModels(str(cardetails[0][23]),True)
        return render_template("UpdateCar.html",cardetails=cardetails,carimages=carimages,car_manufacturer_list=car_manufacturer,car_model_list=carmodels)
    else:
        carimageresponse = {}
        carupdateresponse = Cars().updateCar(request.form,carid)
        print('response')
        print(carupdateresponse)
        if 'ERROR' in carupdateresponse:
            return jsonify(carupdateresponse)
        
        if 'soldout' not in request.form:
            if ('files' not in request.form) and ('files' not in request.files):
                resp = jsonify({'ERROR' : 'No images uploaded'})
                return resp
            else:
                count = 0
                newFilesList = []
                ffiles = request.form.getlist("files")
                for f in ffiles:
                    if f == '/static/image_upload.png':
                        count = count + 1
                    elif not validateFileType(f):
                        resp = jsonify({'ERROR' : 'Invalid file format'})
                        return resp
                    else:
                        newFilesList.append(f)     
            
                if count==5:
                    resp = jsonify({'ERROR' : 'No image selected for uploading'})
                    return resp
                else:
                    print('model')
                    print(request.form)
                    print(request.form.get("txt_model"))
                    carimageresponse = Cars().updateCarImages(carid,newFilesList,request.form.get("txt_model"),request.files)      
        
        if 'ERROR' in carimageresponse:
            return jsonify(carimageresponse)
        else:
            return jsonify(url_for('viewCar',carid=carid)) 
        
@app.route('/Wishlist', methods=["POST","GET"])
def wishlist():
    cardetails = Cars().getWishlistedCars(session["userData"][0][3])
    uniquecardetails = []
    if len(cardetails)>0:
        uniquecardetails = Cars().getUniqueCar(cardetails)
    return render_template("Wishlist.html",cardetails=uniquecardetails,count=len(uniquecardetails)) 

@app.route('/UpdateWishlist/<carid>', methods=["POST","GET"])
def updateWishlist(carid):
    check = Cars().addCarInWishList(session["userData"][0][3],carid)
    return redirect(url_for('homepage',check=check,carid=carid))

@app.route('/ViewCar/<carid>', methods=["POST","GET"])
def viewCar(carid):
    cardetails = Cars().getCars(carid,None,None,None,None,None,None,None,None,None,None,None,None)
    carimages = Cars().getCarImages(carid)
    return render_template("ViewCar.html",cardetails=cardetails,carimages=carimages) 

@app.route('/testDelete', methods=["POST"])
def delete():
    if "userid" in request.form:
        Users().deleteUser(request.form)
    elif "carid" in request.form:
        Cars().deleteCar(request.form)
    elif "imageid" in request.form:
        Cars().deleteCarImage(request.form)       
    return render_template("Home.html")

@app.route('/DeleteWishlist/<carid>', methods=['POST','GET'])
def deleteWishlist(carid):
    Cars().deleteWishlistedCars(str(session["userData"][0][3]),carid)
    return redirect(url_for('wishlist')) 

@app.route('/ViewListings', methods=["POST","GET"])
def viewListings():
    cardetails = Cars().getCarListings(str(session["userData"][0][3]))
    print('@@@@cardata')
    print(cardetails)
    uniquecardetails = Cars().getUniqueCar(cardetails)
    return render_template("CarListing.html",cardetails=uniquecardetails,count=len(uniquecardetails)) 

@app.route('/UploadCar', methods=['POST','GET'])
def uploadCar():
    if 'files' not in request.files:
        resp = jsonify({'ERROR' : 'No images uploaded'})
        return jsonify(resp)
    else:
        image_folder,file_extensions = DbConUtil.getFileConfig()
        count = 0
        lstFilename = []
        ffiles = request.files.getlist("files")
        modelid = request.form.get("txt_model")
        modelname = Cars().getmodelname(modelid).replace(' ','_')
        maximageId = Cars().getExistingCarImageId()
        maximageId = maximageId[0]
        for f in ffiles:
            if f.filename == '':
                count = count + 1
            if f and validateFileType(f.filename):
                maximageId = maximageId + 1
                ext = f.filename.split('.')[1]
                filename = '_'.join([modelname,str(maximageId),str(session["userData"][0][3])])
                filename = '.'.join([filename,ext]) 
                filename = secure_filename(filename)
                filepath = ''.join([image_folder.replace("'",''),modelname])
                if(not os.path.exists(filepath)):
                    carNewFolder = os.path.join(image_folder.replace("'",''),modelname)
                    os.mkdir(carNewFolder)
                    
                f.save(os.path.join(filepath.replace("'",''), filename))
                lstFilename.append(filename)
            else: 
                if f and not(validateFileType(f.filename)):
                    resp = jsonify({'ERROR' : 'Invalid file format'})
                    return jsonify(resp)
        if count==5:
            resp = jsonify({'ERROR' : 'No image selected for uploading'})
            return jsonify(resp)
    if len(lstFilename)>0: 
        carid = Cars().newCar(request.form,session["userData"][0][3],lstFilename)
        if 'ERROR' in carid:
            return jsonify(carid)
        else:
            return jsonify(url_for('viewCar',carid=carid))
        

@app.route('/EstimatePrice', methods=['POST','GET'])
def estimatePrice():
    estimated_price = Cars().priceEstimator(request.form)
    return jsonify(estimated_price)

@app.route('/GetCurrentDate', methods=['POST','GET'])
def getCurrentDate():
    todaydate = urlopen('http://just-the-time.appspot.com/')
    result = todaydate.read().strip()
    result = result.decode('utf-8')
    return jsonify(result=result)
 
@app.route('/UpdatePassword', methods =['POST','GET'])
def updatePassword(): 
    if request.method == "POST":
        passwordUpdateResponse = Users().userUpdate(request.form,None,request.form['txt_email_id'])
        if passwordUpdateResponse == 'SUCCESS':
            session.pop("userData",None)
            return jsonify(url_for('homepage')) 
        else:
            return jsonify(passwordUpdateResponse)
        
@app.route('/admin', methods =['POST','GET'])
def admin():
    if request.method == "GET":
        car_manufacturer = list(Cars().getCarManufacturer('true',''))
        return render_template("Admin.html",car_manufacturer_list=car_manufacturer)
    if request.method == "POST":
        action = request.form.get('actiontType')
        if action == 'MODEL_UPDATE':
            result = Cars().updateCarData(request.form)
        return jsonify(result = result)
    
@app.route('/SearchAndUpdateRecords', methods=['POST','GET'])
def searchAndUpdaterecords():
    if request.method == "GET":
        form_value = request.args.get('value', type=str)
        table_name = request.args.get('table_name',type=str)
        result = []
        if table_name == 'manufacturer':
            result = list(Cars().getCarManufacturer('',form_value))
        if table_name == 'model':
            result = list(Cars().getCarModels(form_value,''))
        if table_name == 'user':
            result = Users().displayProfile(form_value,'')
        if table_name == 'usercontact':
            result = Users().getUserFromContact(form_value)
            print(result)
        return jsonify(result = result)
    if request.method == "POST":
        form_value = request.form.get('form')
        operation = request.form.get('actionType')
        if operation == 'MANUFACTURER_MODEL_INSERT':
            responseResult = Cars().carManufacturerInsert(request.form)
            manDict = request.form.to_dict()
            manDict["manufacturerName"] = responseResult[0][0]
            responseResult = Cars().carModelInsert(manDict)
        if operation == 'MODEL_INSERT':
            responseResult = Cars().carModelInsert(request.form)
        if operation == 'COLOR_INSERT':
            with open("./static/Car_Color.json",'r+') as colorFile:
                carColorData = json.load(colorFile)
                for color in request.form.get('bodyColorList').split(','):
                    if request.form.get('modelName') in carColorData:
                        carColorData[request.form.get('modelName')].append(color)
                    else:
                        carColorData[request.form.get('modelName')] = [color]
                colorFile.seek(0)
                json.dump(carColorData, colorFile, indent = 4)
            responseResult = 'SUCCESS'
        if 'ERROR' in responseResult:
            return jsonify(responseResult)
        else:
            return jsonify(url_for('admin')) 
        
# main function
if __name__ == '__main__':
    app.run(debug=True)
    
