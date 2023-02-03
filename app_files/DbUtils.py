'''
Created on 19-Feb-2022

@author: Srijan-PC
'''
from datetime import datetime
from Constants import Constants
import json


class DbUtils:
    
    def getMappedUserData(self,userFormData):
         
        userDataDict = {}
        if "txt_firstname" in userFormData:
            userDataDict[Constants.FIRSTNAME] = userFormData.get("txt_firstname")
            
        if "txt_lastname" in userFormData:
            userDataDict[Constants.LASTNAME] = userFormData.get("txt_lastname")
            
        if "txt_email_id1" in userFormData:
            userDataDict[Constants.EMAIL_ID] = userFormData.get("txt_email_id1")
            
        if "txt_email_id" in userFormData:
            userDataDict[Constants.EMAIL_ID] = userFormData.get("txt_email_id")
        
        if "txt_email_id2" in userFormData:
            userDataDict[Constants.EMAIL_ID] = userFormData.get("txt_email_id2")
            
        if "txt_dob" in userFormData:
            userDataDict[Constants.DATE_OF_BIRTH] = userFormData.get("txt_dob")
                    
        if "txt_password" in userFormData:
            userDataDict[Constants.PASSWORD] = userFormData.get("txt_password")
            
        if "txt_password1" in userFormData:
            userDataDict[Constants.PASSWORD] = userFormData.get("txt_password1")      
            
        if "txt_address1" in userFormData:
            userDataDict[Constants.ADDRESS_LINE_1] = userFormData.get("txt_address1")
            
        if "txt_address2" in userFormData:
            userDataDict[Constants.ADDRESS_LINE_2] = userFormData.get("txt_address2")
            
        if "txt_city" in userFormData:
            userDataDict[Constants.CITY] = userFormData.get("txt_city")
            
        if "txt_state" in userFormData:
            userDataDict[Constants.STATE] = userFormData.get("txt_state")
            
        if "txt_zip" in userFormData:
            userDataDict[Constants.ZIP_CODE] = userFormData.get("txt_zip")
                    
        if "txt_country" in userFormData:
            userDataDict[Constants.COUNTRY] = userFormData.get("txt_country")
        else:
            userDataDict[Constants.COUNTRY] = "India"
            
        if "txt_phone_no" in userFormData:
            userDataDict[Constants.CONTACT] = userFormData.get("txt_phone_no")
                   
        userDataDict[Constants.USER_LAST_LOGIN] = datetime.now().strftime("%Y-%m-%d,%H:%M:%S.%f")
        userDataDict[Constants.USER_TYPE] = Constants.CUSTOMER_TYPE
        return userDataDict
    
    
    def getMappedUserDataForUpdate(self,userFormData):
        userDataDict = {}                    
        if "pass" in userFormData:
            userDataDict[Constants.PASSWORD] = userFormData.get("pass")      
            
        if "txt_address1" in userFormData:
            userDataDict[Constants.ADDRESS_LINE_1] = userFormData.get("txt_address1")
            
        if "txt_address2" in userFormData:
            userDataDict[Constants.ADDRESS_LINE_2] = userFormData.get("txt_address2")
            
        if "txt_city" in userFormData:
            userDataDict[Constants.CITY] = userFormData.get("txt_city")
            
        if "txt_state" in userFormData:
            userDataDict[Constants.STATE] = userFormData.get("txt_state")
            
        if "txt_zip" in userFormData:
            userDataDict[Constants.ZIP_CODE] = userFormData.get("txt_zip")
            
        if "txt_country" in userFormData:
            userDataDict[Constants.COUNTRY] = userFormData.get("txt_country")
            
        if "contact" in userFormData:
            userDataDict[Constants.CONTACT] = userFormData.get("contact")
            
        if "txt_newpassword" in userFormData:
            userDataDict[Constants.PASSWORD] = userFormData.get("txt_newpassword")
        
        if "txt_userfirstname" in userFormData:
            userDataDict[Constants.FIRSTNAME] = userFormData.get("txt_userfirstname")
        
        if "txt_userlastname" in userFormData:
            userDataDict[Constants.LASTNAME] = userFormData.get("txt_userlastname")
        
        if "txt_userphone_no" in userFormData:
            userDataDict[Constants.CONTACT] = userFormData.get("txt_userphone_no")
        
        if "txt_useremail_id1" in userFormData:
            userDataDict[Constants.EMAIL_ID] = userFormData.get("txt_useremail_id1") 
            
        return userDataDict
    
    def getMappedCarDetails(self,carFormData,userid):
        carDetailsDict = {}
        if "txt_manufacturer" in carFormData:
            carDetailsDict[Constants.MANUFACTURER] = carFormData.get("txt_manufacturer")
            
        if "txt_model" in carFormData:
            carDetailsDict[Constants.MODEL] = carFormData.get("txt_model")
            
        if "txt_titlestatus" in carFormData:
            carDetailsDict[Constants.TITLE_STATUS] = carFormData.get("txt_titlestatus")
            
        if "txt_build_year" in carFormData:
            carDetailsDict[Constants.BUILD_YEAR] = carFormData.get("txt_build_year")
        
        if "txt_car_condition" in carFormData:
            carDetailsDict[Constants.CAR_CONDITION] = carFormData.get("txt_car_condition")
            
        if "txt_cylinder" in carFormData:
            carDetailsDict[Constants.CYLINDERS] = carFormData.get("txt_cylinder")
            
        if "txt_fuel" in carFormData:
            carDetailsDict[Constants.FUEL] = carFormData.get("txt_fuel")
            
        if "txt_odometer" in carFormData:
            carDetailsDict[Constants.ODOMETER] = carFormData.get("txt_odometer")
            
        if "txt_transmission" in carFormData:
            carDetailsDict[Constants.TRANSMISSION] = carFormData.get("txt_transmission")
            
        if "txt_vin" in carFormData:
            carDetailsDict[Constants.VIN] = carFormData.get("txt_vin")
            
        if "txt_carsize" in carFormData:
            carDetailsDict[Constants.CARSIZE] = carFormData.get("txt_carsize")
            
        if "txt_cartype" in carFormData:
            carDetailsDict[Constants.CARTYPE] = carFormData.get("txt_cartype")
            
        if "txt_color" in carFormData:
            carDetailsDict[Constants.PAINT_COLOR] = carFormData.get("txt_color")    
            
        if "txt_description" in carFormData:
            carDetailsDict[Constants.DESCRIPTION] = carFormData.get("txt_description")
            
        if "txt_reg_state" in carFormData:
            carDetailsDict[Constants.STATES] = carFormData.get("txt_reg_state")
                        
        if "txt_EstimatedPrice" in carFormData:
            carDetailsDict[Constants.PRICE] = carFormData.get("txt_EstimatedPrice")
            
        if "txt_drive" in carFormData:
            carDetailsDict[Constants.DRIVE] = carFormData.get("txt_drive")
            
        carDetailsDict[Constants.USER_ID] = userid  
        carDetailsDict[Constants.POSTING_DATE] = datetime.now()

        return carDetailsDict
    
    
    def getMappedCarDetailsForUpdate(self,carFormData):
        carDetailsDict = {}                 
        if "description" in carFormData:
            carDetailsDict[Constants.DESCRIPTION] = carFormData.get("description")
                        
        if "image_url" in carFormData:
            carDetailsDict[Constants.IMAGE_URL] = carFormData.get("image_url")
            
        if "price" in carFormData:
            carDetailsDict[Constants.PRICE] = carFormData.get("price")
            
        if "soldout" in carFormData:
            carDetailsDict[Constants.SOLD_OUT] = carFormData.get("soldout")
            
        if "txt_sellingprice" in carFormData:
            carDetailsDict[Constants.SELLING_PRICE] = carFormData.get("txt_sellingprice")
                                
        if "txt_description" in carFormData:
            carDetailsDict[Constants.DESCRIPTION] = carFormData.get("txt_description")
            
        if "txt_titlestatus" in carFormData:
            carDetailsDict[Constants.TITLE_STATUS] = carFormData.get("txt_titlestatus")
            
        if "txt_build_year" in carFormData:
            carDetailsDict[Constants.BUILD_YEAR] = carFormData.get("txt_build_year")
        
        if "txt_car_condition" in carFormData:
            carDetailsDict[Constants.CAR_CONDITION] = carFormData.get("txt_car_condition")
            
        if "txt_cylinder" in carFormData:
            carDetailsDict[Constants.CYLINDERS] = carFormData.get("txt_cylinder")
            
        if "txt_fuel" in carFormData:
            carDetailsDict[Constants.FUEL] = carFormData.get("txt_fuel")
            
        if "txt_odometer" in carFormData:
            carDetailsDict[Constants.ODOMETER] = carFormData.get("txt_odometer")
        
        if "txt_transmission" in carFormData:
            carDetailsDict[Constants.TRANSMISSION] = carFormData.get("txt_transmission")
            
        if "txt_vin" in carFormData:
            carDetailsDict[Constants.VIN] = carFormData.get("txt_vin")
            
        if "txt_drive_type" in carFormData:
            carDetailsDict[Constants.DRIVE] = carFormData.get("txt_drive_type")
            
        if "txt_cartype" in carFormData:
            carDetailsDict[Constants.CARSIZE] = carFormData.get("txt_cartype")
        
        if "txt_carsize" in carFormData:
            carDetailsDict[Constants.CARSIZE] = carFormData.get("txt_carsize")
            
        if "txt_reg_state" in carFormData:
            carDetailsDict[Constants.STATE] = carFormData.get("txt_reg_state")
            
        if "txt_color" in carFormData:
            carDetailsDict[Constants.PAINT_COLOR] = carFormData.get("txt_color")
            
        if "txt_EstimatedPrice" in carFormData:
            carDetailsDict[Constants.PRICE] = carFormData.get("txt_EstimatedPrice")
            
        if "txt_purchaseduid" in carFormData:
            carDetailsDict[Constants.BUYER_ID] = carFormData.get("txt_purchaseduid")
                                    
        return carDetailsDict
    
    def getCarImages(self,carimages):
        print(len(carimages))
        cimages = ''
        for i in range(len(carimages)):
            if(cimages == ''):
                cimages = carimages[i][2]
            else:
                cimages = cimages + ',' + carimages[i][2]
        return cimages
        

    def getCarData(self,cardetails,carimages):
        
        cardata = {
            "cardetails" : {
            "carid" : cardetails[0][0],
            "userid" : cardetails[0][1],
            "manufacturer" : cardetails[0][2],
            "model" : cardetails[0][3],
            "titlestatus" : cardetails[0][4],
            "buildyear" : cardetails[0][5],
            "carcondition" : cardetails[0][6],
            "cylinders" : cardetails[0][7],
            "fuel" : cardetails[0][8],
            "odometer" : cardetails[0][9],
            "transmission" : cardetails[0][10],
            "vin" : cardetails[0][11],
            "drive" : cardetails[0][12],
            "carsize" : cardetails[0][13],
            "cartype" : cardetails[0][14],
            "paintcolor" : cardetails[0][15],
            "description" : cardetails[0][16],
            "state" : cardetails[0][17],
            "price" : cardetails[0][20],
            "carimages" : {}
            }
        }
        print(cardata["cardetails"])
        for i in range(len(carimages)):
            cindex = "image"+str(i)
            cardata["cardetails"]["carimages"][cindex] = carimages[i]
            
        return cardata
     
    def getMappedDataForModelInsert(self,formData,modelName,modelStatus):
        modelDetailsDict = {}                 
        if "manufacturerName" in formData:
            modelDetailsDict[Constants.MANUFACTURER_ID] = formData.get("manufacturerName")
            
        modelDetailsDict[Constants.MODEL_NAME] = modelName
        modelDetailsDict[Constants.IS_ACTIVE] = modelStatus
                                    
        return modelDetailsDict
    
    def getMappedDataForManfInsert(self,formData,mstatus):
        mDetailsDict = {}                 
        if "manufacturerName" in formData:
            mDetailsDict[Constants.MANUFACTURER_NAME] = formData.get("manufacturerName")
        
        mDetailsDict[Constants.IS_ACTIVE] = mstatus
                                    
        return mDetailsDict   