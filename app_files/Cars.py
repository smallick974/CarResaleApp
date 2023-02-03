'''
Created on 19-Feb-2022

@author: Srijan-PC
'''
from DbUtils import DbUtils
import DbConUtil
from Constants import Constants
from DbOperations import insertData, updateData, deleteData, searchData, getCarDetailsWithImage,getWishlishtedCarDetails,getInsertedRecordId,getCarImageId,updateData
from datetime import datetime
import json
from Models import Models
from scipy.sparse import hstack
import os
from werkzeug.utils import secure_filename
from flask_session import Session
from flask import session
from tkinter.tix import Form

class Cars:
    
    def newCar(self,carFormData,userid,lstFilename):
        try:
            carDetailDict = DbUtils().getMappedCarDetails(carFormData,userid)
            insertData(Constants.TABLE_CAR_DETAILS,carDetailDict)
            carid = getInsertedRecordId(userid);
            carimagedict = {}
            for ffname in range(0,len(lstFilename)):
                carimagedict[Constants.USER_ID] = userid
                carimagedict[Constants.CAR_ID] = carid
                carimagedict[Constants.IMAGE_URL] = lstFilename[ffname]                
                insertData(Constants.TABLE_CAR_IMAGE,carimagedict)
            return carid
        except ValueError as v:
            errorData = {}
            errorData["ERROR"] = v.args[0]
            return errorData
    
    def updateCar(self,carFormData,carid):
        try:
            print('%%%%%%%%%%%%%%')
            print(carFormData)
            carDetailDict = DbUtils().getMappedCarDetailsForUpdate(carFormData)
            idDict = {}
            idDict[Constants.CAR_ID] = carid
            print(carDetailDict)
            updateData(Constants.TABLE_CAR_DETAILS, carDetailDict, idDict)
            return 'SUCCESS'
        except ValueError as v:
            errorData = {}
            errorData["ERROR"] = v.args[0]
            return errorData
    
    def deleteCar(self,carFormData):
        idDict = {}
        idDict[Constants.USER_ID] = carFormData.get("userid")
        idDict[Constants.CAR_ID] = carFormData.get("carid")
        deleteData(Constants.TABLE_CAR_DETAILS, idDict)
        
        
    def deleteCarImage(self,carFormData):
        idDict = {}
        idDict[Constants.IMAGE_ID] = carFormData.get("imageid")
        deleteData(Constants.TABLE_CAR_IMAGE, idDict)
        
    def getCarManufacturer(self,isactive,mname):
        idDict = {}
        if isactive=='true':
            idDict[Constants.IS_ACTIVE] = 'true'
        if mname != '':
            idDict['LOWER('+Constants.MANUFACTURER_NAME+')'] = mname.lower()
        car_manufacturer_list = searchData(Constants.TABLE_CAR_MANUFACTURER,'*',idDict)
        return car_manufacturer_list
    
    def getCarModels(self,mid,isactive):
        idDict = {}
        idDict[Constants.MANUFACTURER_ID] = mid
        if isactive == True:
            idDict[Constants.IS_ACTIVE] = 'true'
        car_models_list = searchData(Constants.TABLE_CAR_MODEL,'*',idDict)
        return car_models_list
    
    def getCars(self,carid,manufacturer,model,year,condition,cylinder,fueltype,drivetype,state,size,searchText,minprice,maxprice):
        car_list = getCarDetailsWithImage(None,carid,manufacturer,model,year,condition,cylinder,fueltype,drivetype,state,size,searchText,minprice,maxprice)
        return car_list
    
    def addCarInWishList(self,userid,carid):
        cardict={}
        cardict[Constants.USER_ID] =userid
        cardict[Constants.CAR_ID] = carid
        cardict[Constants.WISH_DATE] = datetime.now().strftime("%Y-%m-%d,%H:%M:%S.%f")
        insertData(Constants.TABLE_WISHLIST,cardict)
        return True
    
    
    def getCarImages(self,carId):
        idDict = {}
        idDict[Constants.CAR_ID] = carId
        cardetails = searchData(Constants.TABLE_CAR_DETAILS, '*', idDict)
        carimagesdata = searchData(Constants.TABLE_CAR_IMAGE, '*', idDict)
        carimages = DbUtils.getCarImages(self,carimagesdata)
        return carimages
    
    def getWishlistedCars(self,userId):
        wishlistedCars = getWishlishtedCarDetails(self,userId)
        return wishlistedCars
    
    def getCarListings(self,userId):
        carList = getCarDetailsWithImage(userId,None,None,None,None,None,None,None,None,None,None,None,None,None)
        return carList
        
    def deleteWishlistedCars(self,userId,carId):
        idDict = {}
        idDict[Constants.USER_ID] = userId
        idDict[Constants.CAR_ID] = carId
        deleteData(Constants.TABLE_WISHLIST, idDict)
        
    def getUniqueCar(self,cardetails):
        uniquecardetails = []
        lstuniquecar = []
        for c in range(0,len(cardetails)):
            if not cardetails[c][0] in lstuniquecar:
                uniquecardetails.append(cardetails[c])
                lstuniquecar.append(cardetails[c][0])
        return uniquecardetails
                
    def priceEstimator(self,carformdata): 
        print(carformdata)
        models = Models()
        year = models.preprocess_year(carformdata.get('txt_build_year'))
        mname = Cars().getmanufacturerName(carformdata.get('txt_manufacturer')).strip()
        manufacturer = models.preprocess_manufacturer(mname)
        print(mname)
        modelname = Cars().getmodelname(carformdata.get('txt_model')).strip()
        model = models.preprocess_model(modelname)
        print(modelname)
        condition = models.preprocess_condition(carformdata.get('txt_car_condition'))        
        cylinders = models.preprocess_cylinders(carformdata.get('txt_cylinder')+" cylinders")        
        fuel = models.preprocess_fuel(carformdata.get('txt_fuel'))        
        odometer = models.preprocess_odometer(carformdata.get('txt_odometer'))        
        transmission = models.preprocess_transmission(carformdata.get('txt_transmission'))        
        drive = models.preprocess_drive(carformdata.get('txt_drive'))        
        cartype = models.preprocess_cartype(carformdata.get('txt_cartype'))        
        paint = models.preprocess_paint_color(carformdata.get('txt_color'))
        statename = carformdata.get('txt_reg_state')
        userstate = Constants.getStateAbbr(self,statename)
        state = models.preprocess_state(userstate)
        
        X_stack = hstack((year, manufacturer, model, condition, cylinders, 
                      fuel, odometer, transmission, drive, cartype, 
                      paint, state))
    
        price_DTR = abs(models.predict_DTR(X_stack))
        price_LGB = abs(models.predict_LGB(X_stack))
        price_LR = abs(models.predict_LR(X_stack))
        average_price = round((price_DTR+price_LGB+price_LR)/3, 0)
        print(price_DTR)
        print(price_LGB)
        print(price_LR)
        print(average_price)
        return average_price 
    
    def getmodelname(self,modelid):
        idDict = {}
        idDict[Constants.MODEL_ID] = modelid
        modelname = searchData(Constants.TABLE_CAR_MODEL,[Constants.MODEL_NAME],idDict)
        print(modelname)
        print(modelid)
        return modelname[0][0]
    
    def getmanufacturerName(self,manid):
        idDict = {}
        idDict[Constants.MANUFACTURER_ID] = manid
        manname = searchData(Constants.TABLE_CAR_MANUFACTURER,[Constants.MANUFACTURER_NAME],idDict)
        print(manname)
        print(manid)
        return manname[0][0]
    
    def getExistingCarImageId(self):
        imageId = getCarImageId(self)
        return imageId
    
    def updateCarImages(self,carId,newFilesList,modelId,imageFiles): 
        try:
            existingFileList = Cars().getCarImages(carId).split(',')
            FilesToDelete = []
            newFileNameList = []
            idDict = {}
            for n in newFilesList:
                fname = n.replace('\\','/').rsplit('/', 1)[1]
                newFileNameList.append(fname)
            
            for e in existingFileList:
                if (not e in newFileNameList) and (not e.rsplit("_", 2)[1] in FilesToDelete):
                    FilesToDelete.append(e)
                    idDict[Constants.IMAGE_ID] = e.rsplit("_", 2)[1]
                    deleteData(Constants.TABLE_CAR_IMAGE,idDict)
         
            modelname = Cars().getmodelname(modelId).replace(' ','_')
            image_folder,file_extensions = DbConUtil.getFileConfig()
            filepath = ''.join([image_folder.replace("'",''),modelname])
            if len(FilesToDelete)>0:
                for delFile in FilesToDelete:
                    os.remove(os.path.join(filepath.replace("'",''), delFile))
            
            maximageId = Cars().getExistingCarImageId()[0]
            lstFilename = []
        
            for fname in imageFiles.getlist("files"):
                maximageId = maximageId + 1
                ext = fname.filename.split('.')[1]
                filename = '_'.join([modelname,str(maximageId),str(session["userData"][0][3])])
                filename = '.'.join([filename,ext])
                filename = secure_filename(filename)            
                fname.save(os.path.join(filepath.replace("'",''), filename))
                lstFilename.append(filename)        
        
            if len(lstFilename) > 0:
                carimagedict = {}
                for ffname in range(0,len(lstFilename)):
                    carimagedict[Constants.USER_ID] = str(session["userData"][0][3])
                    carimagedict[Constants.CAR_ID] = carId
                    carimagedict[Constants.IMAGE_URL] = lstFilename[ffname]                
                    insertData(Constants.TABLE_CAR_IMAGE,carimagedict)
            
            return 'SUCCESS'
        
        except ValueError as v:
            errorData = {}
            errorData["ERROR"] = v.args[0]
            return errorData
        
    def updateCarData(self,formData):
        try:
            idDict = {}
            idDict[Constants.MODEL_ID] = formData.get('form').split('&')[1].split('=')[1].split('_')[0]
            updateDict = {}
            updateDict[Constants.IS_ACTIVE] = formData.get('form').split('&')[2].split('=')[1]
            updateData(Constants.TABLE_CAR_MODEL,updateDict,idDict)
            return 'SUCCESS'
        except ValueError as v:
            errorData = {}
            errorData["ERROR"] = v.args[0]
            return errorData
        
    def carModelInsert(self,formData):
        try:
            for i in formData.get("modelList").split(','):
                modelMappedData = DbUtils().getMappedDataForModelInsert(formData,i,True)
                insertData(Constants.TABLE_CAR_MODEL, modelMappedData)
            return 'SUCCESS'
        except ValueError as v:
            errorData = {}
            errorData["ERROR"] = v.args[0]
            return errorData
            
    def carManufacturerInsert(self,formData):
        try:
            manMappedData = DbUtils().getMappedDataForManfInsert(formData,True)
            insertData(Constants.TABLE_CAR_MANUFACTURER, manMappedData)
            manList = Cars().getCarManufacturer(True,manMappedData[Constants.MANUFACTURER_NAME])
            return manList
        except ValueError as v:
            errorData = {}
            errorData["ERROR"] = v.args[0]
            return errorData       