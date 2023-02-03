'''
Created on 19-Feb-2022

@author: Srijan-PC
'''

from DbOperations import insertData, searchData, updateData, deleteData
from DbUtils import DbUtils
from Constants import Constants
from PasswordUtil import PasswordUtil


class Users:

    def userSignUp(self,userFormData):
        useremaildict = {}
        useremaildict[Constants.EMAIL_ID] = userFormData["txt_email_id1"]
        emailid = searchData(Constants.TABLE_USER_DETAILS,[Constants.EMAIL_ID],useremaildict)
        useremaildict1 = {}
        useremaildict1[Constants.CONTACT] = userFormData["txt_phone_no"]
        contactno = searchData(Constants.TABLE_USER_DETAILS,[Constants.CONTACT],useremaildict1)
        try:
            print(len(emailid))
            if len(emailid) != 0:
                raise ValueError("This Email ID already exists..")
            if len(contactno) != 0:
                raise ValueError("User already registered with this contact number")
            else:
                print('in else')
                dbUtil = DbUtils()
                pUtil = PasswordUtil()
                print(userFormData.get('txt_password1'))
                password = pUtil.getHashedPassword(userFormData.get('txt_password1'))
                print(password.decode()) 
                
                userDataDict = dbUtil.getMappedUserData(userFormData)
                print(userDataDict)
                userDataDict[Constants.PASSWORD] = password.decode()
                print(userDataDict)
                insertData(Constants.TABLE_USER_DETAILS,userDataDict)
                return 'SUCCESS'
        except ValueError as v:
            error = {}
            error["ERROR"] = v.args[0]
            return error
        except Exception as e:
            error = {}
            error["ERROR"] = e
            return error    
    
    def userLogin(self,userFormData):
        dbUtil = DbUtils()
        loginDict = dbUtil.getMappedUserData(userFormData) 
        credDict = {} 
        credDict[Constants.EMAIL_ID] = loginDict["emailid"]            
        loginData = searchData(Constants.TABLE_USER_DETAILS,[Constants.FIRSTNAME,Constants.EMAIL_ID,Constants.USER_LAST_LOGIN,Constants.USER_ID,Constants.PASSWORD,Constants.USER_TYPE],credDict)
        idDict = {}
        pUtil = PasswordUtil()
        try:
            if pUtil.matchPassword(loginDict["pass"],loginData[0][4]) == 0:
                raise ValueError("Email ID or Password Incorrect..")
            else:
                idDict[Constants.USER_ID] = loginData[0][3]
                timestampDict = {}
                timestampDict[Constants.USER_LAST_LOGIN] = loginDict[Constants.USER_LAST_LOGIN]
                updateData(Constants.TABLE_USER_DETAILS,timestampDict,idDict)
                return loginData
        except ValueError as v:
            loginData = {}
            loginData["Error"] = v.args[0]
            return loginData
            
    
    
    def userUpdate(self,userFormData,userid,emailid):
        print(userFormData)
        userDetails = DbUtils().getMappedUserDataForUpdate(userFormData)
        idDict = {}
        
        if userid != None:
            idDict[Constants.USER_ID] = userid
        if emailid != None:
            idDict[Constants.EMAIL_ID] = emailid 
        try:
            if Constants.PASSWORD in userDetails:
                pUtil = PasswordUtil()
                userDetails[Constants.PASSWORD] = pUtil.getHashedPassword(userDetails[Constants.PASSWORD]).decode()      
            updateData(Constants.TABLE_USER_DETAILS,userDetails,idDict)
            return 'SUCCESS'
        except Exception as e:
            print(e)
            loginData = {}
            loginData["ERROR"] = 'Error in updating record'
            return loginData
            print('Data update>> ')
        
    def deleteUser(self,userFormData):
        idDict = {}
        idDict[Constants.USER_ID] = userFormData.get("userid")
        try:
            deleteData(Constants.TABLE_USER_DETAILS, idDict)
        except Exception as e:
            print(e)
            
    def displayProfile(self,emailid,userid):
        emailDict={}
        try:
            if emailid!=None:
                emailDict[Constants.EMAIL_ID] = emailid    
                profiledata = searchData(Constants.TABLE_USER_DETAILS,[Constants.FIRSTNAME,Constants.LASTNAME,Constants.EMAIL_ID,Constants.CONTACT,Constants.DATE_OF_BIRTH,Constants.ADDRESS_LINE_1,Constants.ADDRESS_LINE_2,Constants.CITY,Constants.STATE,Constants.ZIP_CODE,Constants.COUNTRY,Constants.USER_ID],emailDict)
            else:
                emailDict[Constants.USER_ID] = userid
                profiledata = searchData(Constants.TABLE_USER_DETAILS,[Constants.FIRSTNAME,Constants.LASTNAME,Constants.EMAIL_ID,Constants.CONTACT],emailDict)      
            if len(profiledata) == 0:
                raise ValueError
            else:
                return profiledata
        except ValueError:
            print("No Data Found..")
        pass        
        
    def getUserFromContact(self,contactno):
        try:
            usercontactdict1 = {}
            usercontactdict1[Constants.CONTACT] = contactno
            contactno = searchData(Constants.TABLE_USER_DETAILS,[Constants.CONTACT,Constants.FIRSTNAME,Constants.LASTNAME,Constants.USER_ID],usercontactdict1)
            if len(contactno) == 0:
                raise ValueError
            else:
                return contactno
        except ValueError:
            print("No Data Found..")
        pass     