# PCA and K-Means

1. Create KMeans classifier. 

For testing:

(a) Create two numpy arrays (resting, stressed) with 1,000 samples each: μrest =
[60, 10], Σrest = [[20, 100], [100, 20]]. μstress = [100, 80], Σstress = [[50, 20], [20, 50]].

(b) Run k-means clustering algorithm on that data

(c) Plot the resulting centroids of each clusters and the data.

(d) Test your algorithm against Sklearn’s KMeans algorithm for comparison

2. Create PrincipleComponentAnalysis class.

For testing:
    
(a) Read in the iris dataset 

(b) Drop all nans and only look at the columns: ”sepal length”,”sepal width”,
’petal length’,’petal width’,’species’

(c) Run manual PCA on this code with a threshold of 0.95

(d) Print resulting projection matrix

(e) Test manual algorithm against Sklearn’s PCA


3. Using the pokemon dataset.csv classify a pokemon as a legendary or non-legendary using a Support Vector
Machine from Sklearn without the use the pokemon’s name or name2 as features.
