Homework Details:

Build a neural network from scratch using Python!

In this homework, you need to implement a neural network class in Python without using any framework library (i.e., tensorflow, keras, pytorch etc.). You can use numpy, pandas, math or any helper libraries.

Your neural network class should have following properties:
- Parametric input size
- Parametric output size
- Just implement fully connected layers; any number of such layers can be added
(Let’s keep it simple, no convolution, recurrent or other types of layers are needed!)
- At least 2 activation function alternatives for each layer (i.e., tanh, sigmoid)
- At least 2 loss function alternatives for output layer (i.e., mse, rmse)
- It should print training errors during training.

Your neural network should have any necessary methods/functions of your choice. But do not forget to include the following method/function names:
- fit/train: trains the neural network
- predict: makes prediction for the input data

Using your neural network class, train a neural network and make predictions on data to show the working and performance of your implementation. You should
submit the data you used with a file name: nn_data.csv

Optionally, you can implement a softmax function for the output layer that identifies which prediction class is the output. By using the softmax function, it will be easy to understand the output of the predictions.