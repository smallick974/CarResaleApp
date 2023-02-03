'''
Created on 06-Mar-2022

@author: Srijan-PC
'''

import math
import random
import smtplib
from email.mime.text import MIMEText
import http.client
import mimetypes
from Constants import Constants
from DbOperations import searchData

class ResetPassword:
    
    def generateOTP(self):
        OTPDigits = "0123456789"
        OTP = ""
        for i in range(6):
            OTP += OTPDigits[math.floor(random.random()*10)] 
        return OTP

    def sendEmail(self,emailid,otp):        
        try:
            useremaildict = {}
            useremaildict[Constants.EMAIL_ID] = emailid
            emailidverify = searchData(Constants.TABLE_USER_DETAILS,[Constants.EMAIL_ID],useremaildict)
            if len(emailidverify) == 0:
                raise ValueError("User is not registered with this email ID")
            else:
                sender = "password_reset@zohomail.in"
                message = MIMEText("Hi,\n\nPlease enter this OTP to reset your password: " + otp + "\n\nRegards,\nPassword Reset Team")
                message['Subject'] = "Password Reset" 
                message['From'] = sender 
                message['To'] = emailid
                message['Signature'] = "Password Reset Team"        
                smtpcon = smtplib.SMTP_SSL('smtp.zoho.in',465)
                smtpcon.login(sender, 'tznafbdc4b49') 
                smtpcon.sendmail(sender, [emailid], message.as_string()) 
                smtpcon.quit()
                
                return 'SUCCESS'
        except ValueError as v:
            error = {}
            error["ERROR"] = v.args[0]
            return error
        except Exception as e:
            print("Exception: ",e)
            error = {}
            error["ERROR"] = 'Error in sending OTP'
            return error
        
        
