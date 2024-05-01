# Univariate and Multi-Variate Discriminants

1. Created Gaussian discriminant class (univariate) and tested it.

For testing:

(a) Created two numpy arrays (resting, stressed), where resting data has a mean of
60 and stdev. of 5 and stressed has a mean of 100 and stdev. of 5.

(b) Fited a uni-variate Guassian to each array

(c) Plotted the resulting discriminant values for inputs (x) 40 to 120 


2. Created Gaussian discriminant class (Multivariate).

For testing:
    
(a) Created two numpy arrays (resting, stressed) that have two features each. μrest =
[60, 10], Σrest = [[20, 100], [100, 20]]. μstress = [100, 80], Σstress = [[50, 20], [20, 50]]

(b) Fitted a multivariate gaussian discriminant to each array

(c) Plot the resulting discriminant values for inputs (x) [20,20] to [120,120] and
the decision boundary 

3. Create Discriminant Classifier class. 


For testing:
    
(a) Using the multivariate discriminants created in problem 2, plot the decisions
the discriminant classifier outputs for inputs (x) [20,20] to [120,120]. 

(b) First, created a pooled covariance matrix (shared class covariance) and replotted decisions 

(c) Still using the pooled covariance matrix changed the priors of a class for exploration.
