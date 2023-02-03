'''
Created on 19-Feb-2022

@author: Srijan-PC
'''

# returns a dictionary based on database.ini file

from configparser import ConfigParser
import psycopg2

# get section and update dictionary with connection string key:value pairs
def config(section,conf_file='database.ini'): 
    parser = ConfigParser()  # to parse database configuration file   
    parser.read(conf_file)   # read database.ini file    
    try:
        db = {}
        if section in parser:
            for key in parser[section]:
                db[key] = parser[section][key]           
        return db  
    except Exception as e:
            print(e)
            
# connect to PostgreSQL database         
def connectDB():
    try:
        dbValues = config('db_connection')
        port = dbValues['port']
        username = dbValues['username']
        password = dbValues['password']
        hostname = dbValues['hostname']        
        database = dbValues['database']
        
        con = psycopg2.connect(host=hostname, database=database, user=username, password=password, port=port)
        cursor = con.cursor()
        return con,cursor          
    except Exception as e:
        print(e)
        
def getFileConfig():
    try:
        fvalues = config('file_uploads')
        folder = fvalues['image_folder']
        validExt = fvalues['valid_extensions']
        return folder,validExt
    except Exception as e:
        print(e)
        