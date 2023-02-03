'''
Created on 23-Feb-2022

@author: Srijan-PC
'''

import pickle
from scipy.sparse import hstack
import numpy as np

class Models:
    
    def __init__(self):
        self.year = "./model_files/data_processing/year_scaler"
        self.manufacturer = "./model_files/data_processing/manufacturer_onehot_encoder"
        self.model = "./model_files/data_processing/dict_model_freq"
        self.condition = "./model_files/data_processing/condition_onehot_encoder"
        self.cylinders = "./model_files/data_processing/cylinders_dict"
        self.fuel = "./model_files/data_processing/fuel_onehot_encoder"
        self.odometer = "./model_files/data_processing/odometer_scaler"
        self.transmission = "./model_files/data_processing/transmission_onehot_encoder"
        self.drive = "./model_files/data_processing/drive_onehot_encoder"
        self.cartype = "./model_files/data_processing/cartype_onehot_encoder"
        self.paint_color = "./model_files/data_processing/paint_color_ordinal_encoder"
        self.state = "./model_files/data_processing/state_ordinal_encoder"
        
        self.dtr = "./model_files/models/Decision_Tree_Regressor"
        self.lgb = "./model_files/models/LGBM_Regressor"
        self.lr = "./model_files/models/Linear_Regression"
        
    
    def preprocess_year(self,year):
        year_scaler = pickle.load(open(self.year,'rb'))
        value = year_scaler.transform(np.array(year).reshape(-1,1)).ravel()
        return value
    
    def preprocess_manufacturer(self,manufacturer):
        manufacturer_onehot_encoder = pickle.load(open(self.manufacturer,'rb'))
        value = manufacturer_onehot_encoder.transform(np.array(manufacturer).reshape(-1,1))
        return value
    
    def preprocess_model(self,model):
        dict_model_freq = pickle.load(open(self.model,'rb'))
        value = 0
        if model in dict_model_freq.keys():
            value = dict_model_freq[model]
        return value
    
    def preprocess_condition(self,condition):
        condition_onehot_encoder = pickle.load(open(self.condition,'rb'))
        value = condition_onehot_encoder.transform(np.array(condition).reshape(-1,1))
        return value
    
    def preprocess_cylinders(self,cylinders):
        cylinders_dict = pickle.load(open(self.cylinders,'rb'))
        value = 0
        if cylinders in cylinders_dict.keys():
            value = cylinders_dict[cylinders]
        return value
    
    def preprocess_fuel(self,fuel):
        fuel_onehot_encoder = pickle.load(open(self.fuel,'rb'))
        value = fuel_onehot_encoder.transform(np.array(fuel).reshape(-1,1))
        return value
    
    def preprocess_odometer(self,odometer):
        odometer_scaler = pickle.load(open(self.odometer,'rb'))
        value = odometer_scaler.transform(np.array(odometer).reshape(-1,1)).ravel()
        return value

    def preprocess_transmission(self,transmission):
        transmission_onehot_encoder = pickle.load(open(self.transmission,'rb'))
        value = transmission_onehot_encoder.transform(np.array(transmission).reshape(-1,1))
        return value

    def preprocess_drive(self,drive):
        drive_onehot_encoder = pickle.load(open(self.drive,'rb'))
        value = drive_onehot_encoder.transform(np.array(drive).reshape(-1,1))
        return value
    
    def preprocess_cartype(self,cartype):
        cartype_onehot_encoder = pickle.load(open(self.cartype,'rb'))
        value = cartype_onehot_encoder.transform(np.array(cartype).reshape(-1,1))
        return value
    
    def preprocess_paint_color(self,paint_color):
        paint_color_ordinal_encoder = pickle.load(open(self.paint_color,'rb'))
        value = paint_color_ordinal_encoder.transform(np.array(paint_color).reshape(-1,1)).ravel()
        return value
    
    def preprocess_state(self,state):
        state_ordinal_encoder = pickle.load(open(self.state,'rb'))
        value = state_ordinal_encoder.transform(np.array(state).reshape(-1,1)).ravel()
        return value




    # 1. Decision Tree Regressor
    def predict_DTR(self,x):
        dtr = pickle.load(open(self.dtr,'rb'))
        y = dtr.predict(x)
        return y[0]
    
    # 2. LGBM Regressor
    def predict_LGB(self,x):
        lgb = pickle.load(open(self.lgb,'rb'))
        y = lgb.predict(x)
        return y[0]
    
    # 3. Linear Regression
    def predict_LR(self,x):
        lr = pickle.load(open(self.lr,'rb'))
        y = lr.predict(x)
        return y[0]
    
if __name__ == '__main__':
    models = Models()
    
    year = models.preprocess_year("2000")
    print("year: ",year)
    
    manufacturer = models.preprocess_manufacturer("Maruti")
    print("manufacturer: ",manufacturer)
    
    model = models.preprocess_model("Wagon R VXI")
    print("model: ",model)
    
    condition = models.preprocess_condition("Excellent")
    print("condition: ",condition)
    
    cylinders = models.preprocess_cylinders("3 cylinders")
    print("cylinders: ",cylinders)
    
    fuel = models.preprocess_fuel("Petrol")
    print("fuel: ",fuel)
    
    odometer = models.preprocess_odometer("83000")
    print("odometer: ",odometer)
    
    transmission = models.preprocess_transmission("Manual")
    print("transmission: ",transmission)
    
    drive = models.preprocess_drive("FWD")
    print("drive: ",drive)
    
    cartype = models.preprocess_cartype("Hatchback")
    print("cartype: ",cartype)
    
    paint = models.preprocess_paint_color("white")
    print("paint_color: ",paint)
    
    state = models.preprocess_state("MH")
    print("state: ",state)
    
    
    # Encoding all the features
    
    X_stack = hstack((year, manufacturer, model, condition, cylinders, 
                      fuel, odometer, transmission, drive, cartype, 
                      paint, state))
    
    x = models.predict_DTR(X_stack)
    print(x)
    
    y = models.predict_LGB(X_stack)
    print(y)
    
    z = models.predict_LR(X_stack)
    print(z)
    average_price = round((x+y+z)/3, 0)
    print(average_price)
