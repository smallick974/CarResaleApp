'''
Created on 19-Feb-2022

@author: Srijan-PC
'''

class Constants:
    
    # User Database constants
    FIRSTNAME = 'firstname'
    LASTNAME = 'lastname'
    EMAIL_ID = 'emailid'
    PASSWORD = 'pass'
    DATE_OF_BIRTH = 'dob'
    ADDRESS_LINE_1 = 'addr_1'
    ADDRESS_LINE_2 = 'addr_2'
    CITY = 'city'
    STATE = 'states'
    ZIP_CODE = 'zip'
    COUNTRY = 'country'
    CONTACT = 'contact'
    USER_LAST_LOGIN = 'last_login'
    USER_ID = 'userid'
    TABLE_USER_DETAILS = 'userdetails'
    
    
    #Car Database Constants
    TABLE_CAR_DETAILS = 'cardetails'
    TABLE_CAR_IMAGE = 'carimage'
    MANUFACTURER = 'manufacturer'
    MODEL = 'model'
    TITLE_STATUS = 'title_status'
    BUILD_YEAR = 'buildyear'
    CAR_CONDITION = 'carcondition'
    CYLINDERS = 'cylinders'
    FUEL = 'fuel'
    ODOMETER = 'odometer'
    TRANSMISSION = 'transmission'
    VIN = 'vin'
    DRIVE = 'drive'
    CARSIZE = 'carsize'
    CARTYPE = 'cartype'
    PAINT_COLOR = 'paint_color'
    DESCRIPTION = 'description'
    STATES = 'states'
    IMAGE_URL = 'image_url'
    POSTING_DATE = 'posting_date'
    PRICE = 'price'
    CAR_ID = 'carid'
    IMAGE_ID = 'imageid'
    
    TABLE_CAR_MANUFACTURER = 'carmanufacturer'
    TABLE_CAR_MODEL = 'carmodel'
    TABLE_WISHLIST = 'wishlist'
    MANUFACTURER_NAME = 'mname'
    IS_ACTIVE = 'isactive'
    MANUFACTURER_ID = 'manufacturerid'
    WISH_DATE = 'wishdate'
    
    USER_TYPE = 'user_type'
    CUSTOMER_TYPE = 'Customer'
    SOLD_OUT = 'sold_out'
    SELLING_PRICE = 'selling_price'
    MODEL_NAME = 'modelname'
    MODEL_ID = 'modelid'
    BUYER_ID = 'purchased_uid'
    def getStateAbbr(self,statename):
        statedict = {'AN':'Andaman and Nicobar Islands','AP':'Andhra Pradesh','AR':'Arunachal Pradesh','AS':'Assam','BR':'Bihar','CH':'Chandigarh','CG':'Chhattisgarh','DH':'Dadra and Nagar Haveli',
    'DD':'Daman and Diu','DL':'Delhi','GA':'Goa','GJ':'Gujarat','HR':'Haryana','HP':'Himachal Pradesh','JK':'Jammu and Kashmir','JH':'Jharkhand','KA':'Karnataka','KL':'Kerala','LD':'Lakshadweep',
    'MP':'Madhya Pradesh','MH':'Maharashtra','MN':'Manipur','ML':'Meghalaya','MZ':'Mizoram','NL':'Nagaland','OR':'Orissa','PY':'Pondicherry','PB':'Punjab','RJ':'Rajasthan','SK':'Sikkim',
    'TN':'Tamil Nadu','TR':'Tripura','UP':'Uttar Pradesh','UK':'Uttarakhand','WB':'West Bengal'}
        
        statekeys = list(statedict.keys())
        statevalue = list(statedict.values())
        stateindex = statevalue.index(statename)
        return statekeys[stateindex]
    
        