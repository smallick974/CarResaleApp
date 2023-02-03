'''
Created on 28-Mar-2022

@author: Srijan-PC
'''

import bcrypt

class PasswordUtil:
    
    def getHashedPassword(self,password):
        saltedpasswd = bcrypt.gensalt()
        hashedpassws = bcrypt.hashpw(password.encode('utf-8'),saltedpasswd)
        return hashedpassws
    
    def matchPassword(self,userpassword,hashedpassws):
        
        if bcrypt.checkpw(userpassword.encode('utf-8'),hashedpassws.encode('utf-8')):
            return 1
        else:
            return 0