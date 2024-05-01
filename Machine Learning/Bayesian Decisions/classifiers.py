''' Import Libraries'''
import pandas as pd
import numpy as np


class Classifier:
    ''' This is a class prototype for any classifier. It contains two empty methods: predict, fit'''
    def __init__(self):
        self.model_params = {}
        pass
    
    def predict(self, x):
        '''This method takes in x (numpy array) and returns a prediction y'''
        raise NotImplementedError
    
    def fit(self, x, y):
        '''This method is used for fitting a model to data: x, y'''
        raise NotImplementedError



            
class Prior(Classifier):
    
    def __init__(self):
        super().__init__()
        self.model_params = {}
        pass
    
    def calculated_prior(self,y):
        class_types, count = np.unique(y, return_counts = True)
        total = len(y)
        value = count/total
        return dict(zip(class_types, value))

    def predict(self, x):
        pred = [max(self.model_params, key = lambda c: self.model_params[c]) for i in range (len(x))]
        return np.array(pred)
        
    
    def fit(self, x, y):
        self.model_params = self.calculated_prior(y)
        return self
         
        
