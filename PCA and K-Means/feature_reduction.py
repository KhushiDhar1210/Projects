import numpy as np
import matplotlib.pyplot as plt

class FeatureReduction():
    
    def __init__(self):
        self.model_params = {}
    
    def fit(self, data):
        pass
    
    def predict(self, data):
        pass
    

import numpy as np

class PrincipleComponentAnalysis(FeatureReduction):
    '''self.model_params is where you will save your principle components (up to LoV)'''
    ''' Its useful to use a projection matrix as your only param'''
    def fit(self, data, thresh=0.95, plot_var=True):
       
        standardized_data = (data - np.mean(data, axis=0)) / np.std(data, axis=0)
        
        cov_matrix = np.cov(standardized_data.T)
        eigen_values, eigen_vectors = np.linalg.eig(cov_matrix)
    
        
        idx = np.argsort(eigen_values)[::-1]
    
        eigen_values = eigen_values[idx]
        eigen_vectors = eigen_vectors[:, idx]
    
    
        cumulative_variance_ratio = np.cumsum(eigen_values) / np.sum(eigen_values)
    
    
        n_components = np.argmax(cumulative_variance_ratio >= thresh) + 1
    
    
        self.model_params['Projection Matrix'] = eigen_vectors[:, :n_components]
    

   
    def predict(self, data):
        return data.dot(self.model_params['Projection Matrix'])
    
    def calc_variance_explained(self, eigen_values):
        '''Input: list of eigen values
           Output: list of normalized values corresponding to percentage of information an eigen value contains'''
        
        variance_explained = eigen_values / np.sum(eigen_values)
        
        return variance_explained
