'''
Created on 19-Feb-2022

@author: Srijan-PC
'''

from DbConUtil import connectDB
import json

def insertData(tableName,dataDict):
    try:
        con,cursor = connectDB()
        query = "insert into mca." + tableName + " (" + ",".join(dataDict.keys()) + ")"  + " values(" + ",".join(["%s"] * len(dataDict.keys())) + ")"
        cursor.executemany(query,(list(dataDict.values()),))
        con.commit()
        cursor.close()
        con.close()
    except Exception as e:
        raise ValueError("Error in saving record")
        
    

def updateData(tableName,updateDict,idDict):
    try:
        con,cursor = connectDB()
        if "userid" in idDict:
            idDict["userid"] = str(idDict.get("userid"))
        if "emailid" in idDict:
            idDict["emailid"] = idDict["emailid"]
        query = "update mca." + tableName + " set " + "" + " , ".join(name +" = " +"'"+updateDict[name]+"'" for name in updateDict) + " where "+" and ".join(idn +" = " + "'" + idDict[idn] + "'" for idn in idDict)
        cursor.execute(query)
        con.commit()
        cursor.close()
        con.close()
    except Exception as e:
        raise ValueError("Error in updating record")
    
    
def searchData(tableName,columnName,dictName):
    try:
        con,cursor = connectDB()
        if dictName=={}:
            query = "select " + ",".join(columnName) +" from mca."+ tableName
        else:
            query = "select " + ",".join(columnName) +" from mca."+ tableName +" where " + " and ".join(name +" = " +"'"+dictName[name]+"'" for name in dictName)
        cursor.execute(query)
        data = cursor.fetchall()
        return data
        con.commit()
        cursor.close()
        con.close()
    except Exception as e:
        print(e)
    

def deleteData(tableName,idDict):
    try:
        con,cursor = connectDB()
        query = "delete from mca." + tableName + " where "+" and ".join(idn +" = " + "'" + idDict[idn] + "'" for idn in idDict)
        cursor.execute(query)
        con.commit()
        cursor.close()
        con.close() 
    except Exception as e:
        print(e)

    
def getCarDetailsWithImage(userid,carid,manufacturer,model,year,condition,cylinder,fueltype,drivetype,state,size,searchText,minprice,maxprice):
    try:
        con,cursor = connectDB()
        if(userid != None):
            query = "select distinct cd.carid,cm.mname,m.modelname,cd.price,ci.image_url,cd.description,cm.manufacturerid,cd.sold_out,cd.selling_price,cd.purchased_uid from mca.cardetails cd,mca.carimage ci,mca.carmanufacturer cm,mca.carmodel m where cd.carid=ci.carid and cd.manufacturer=cm.manufacturerid and cd.model=m.modelid and (cd.userid="+userid+" or cd.purchased_uid='"+userid+"');"
        elif(carid != None):
            query = "select * from mca.cardetails cd,mca.carmanufacturer cm,mca.carmodel m where cd.manufacturer=cm.manufacturerid and cd.model=m.modelid and cd.carid="+carid+";"
        else:
            query = "select distinct cd.carid,cm.mname,m.modelname,cd.price,ci.image_url,cd.buildyear,cd.carcondition,cd.cylinders,cd.fuel,cd.drive,cd.states,cd.carsize,cm.manufacturerid,cd.sold_out,m.modelId from mca.cardetails cd,mca.carimage ci,mca.carmanufacturer cm,mca.carmodel m where cd.carid=ci.carid and cd.manufacturer=cm.manufacturerid and cd.model=m.modelid and cd.sold_out=false"
            if(manufacturer!=None and manufacturer!=''):
                query = query + " and cd.manufacturer IN ("+manufacturer+")"
            if(model!=None and model!='' ):
                query = query + " and cd.model IN ("+model+")"
            if(year!=None and year!=''):
                query = query + " and cd.buildyear IN ("+year+")"
            if(condition!=None and condition!=''):
                query = query + " and cd.carcondition IN ("+condition+")"
            if(cylinder!=None and cylinder!=''):
                query = query + " and cd.cylinders IN ("+cylinder+")"
            if(fueltype!=None and fueltype!=''):
                query = query + " and cd.fuel IN ("+fueltype+")"
            if(drivetype!=None and drivetype!=''):
                query = query + " and cd.drive IN ("+drivetype+")"
            if(state!=None and state!=''):
                query = query + " and cd.states IN ("+state+")"
            if(size!=None and size!=''):
                query = query + " and cd.carsize IN ("+size+")"
            if(minprice!=None and minprice!=''):
                query = query + " and price >= "+minprice
            if(maxprice!=None and maxprice!=''):
                query = query + " and price <= "+maxprice
            if(searchText!=None and searchText!=''):
                lowerSearchText = searchText.lower()
                query = query + " and (LOWER(cm.mname) like '%" + lowerSearchText + "%' or LOWER(m.modelname) like '%" + lowerSearchText + "%')"
            query = query + ";"
        cursor.execute(query)
        data = cursor.fetchall()
        
        con.commit()
        cursor.close()
        con.close()
        return data
    except Exception as e:
        print(e)
    
def getWishlishtedCarDetails(self,userId):
    con,cursor = connectDB()
    query = "select distinct cd.carid,cm.mname,m.modelname,cd.price,w.userid,w.carid,ci.image_url,cd.description,cd.sold_out from mca.cardetails cd,mca.wishlist w, mca.carimage ci, mca.carmanufacturer cm, mca.carmodel m where cd.carid=w.carid and cd.manufacturer=cm.manufacturerid and cd.model=m.modelid and w.userid="+str(userId)+" and ci.carid=cd.carid;" 
    cursor.execute(query)
    data = cursor.fetchall()
    return data
    con.commit()
    cursor.close()
    con.close()  

def getInsertedRecordId(userid):
    con,cursor = connectDB()
    query = "select max(carid) from mca.cardetails where userid ="+str(userid)+";" 
    cursor.execute(query)
    data = cursor.fetchone()
    con.commit()
    cursor.close()
    con.close()
    return data   

def getCarImageId(self):
    con,cursor = connectDB()
    query = "SELECT last_value from mca.carimage_imageid_seq;" 
    cursor.execute(query)
    data = cursor.fetchone()
    con.commit()
    cursor.close()
    con.close()
    return data     
# for debug
if __name__ == '__main__':
    pass

