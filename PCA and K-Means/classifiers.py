import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix

class Classifier:
    ''' This is a class prototype for any classifier. It contains two empty methods: predict, fit'''
    def __init__(self):
        self.model_params = {}
        pass
    
    def predict(self, x):
        '''This method takes in x (numpy array) and returns a prediction y'''
        raise NotImplementedError
    
    def fit(self, dataframe):
        '''This method is used for fitting a model to data: x, y'''
        raise NotImplementedError



class KMeans(Classifier):
    def __init__(self, n_clust, max_iters=100):
        self.n_clust = n_clust
        self.max_iters = max_iters

    def fit(self, X):
        self.centroids = X[np.random.choice(X.shape[0], self.n_clust, replace=False)]
        for _ in range(self.max_iters):
            clust = [[] for _ in range(self.n_clust)]
            for m in X:
                dist = [np.linalg.norm(m - centre) for centre in self.centroids]
                i = np.argmin(dist)
                clust[i].append(m)
            new_centroids = [np.mean(cluster, axis=0) if cluster else centre for centre, cluster in zip(self.centroids, clust)]
            if np.allclose(self.centroids, new_centroids):
                break
            self.centroids = new_centroids
        self.centroids = np.array(self.centroids)  
        self.cluster_centers_ = self.centroids  

    def predict(self, X):
        dist = np.array([[np.linalg.norm(m - centre) for centre in self.centroids] for m in X])
        return np.argmin(dist, axis=1)
