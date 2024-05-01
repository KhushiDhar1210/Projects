# Neural Networks

Code a neural network only using the numpy library from scratch. 


1. A base class Layer with method functions init, forward propagation, and back-
ward propagation. 

2. A class FCLayer that inherits from the base class which is a fully connected/dense
layer. 

(a) The init function will randomly initialize the weights and biases of the layer. 
(b) The forward propagation method takes in an numpy array and returns the output of the layer. 
(c) The backward propagation method takes in an output error and learning rate and returns the input error.

3. A class ActivationLayer that inherits from the base class. 

(a) The init function specifies the activation function to use and its corresponding derivative.
(b) The forward propagation method takes in an numpy array and returns the
output of the layer. 
(c) The backward propagation method takes in an output error and learning rate and returns the input error.

4. A class Network with four methods: init, add, predict, and fit. 

Testing the implementation:

(a) Create individual tests for each object class (i.e., FCLayer and Ac-
tivationLayer). 

(b) Test network class 

(c) Generate Validation Loss curves for an Exclusive Or function with own train/test data

(d) Generate Validation Loss curves for classifying data as stress/not stressed.
– mustress = [120, 35], Σstress =
[1 0
0 1
]
– munotstress = [60, 50], Σnotstress =
[1 1
1 1
]

