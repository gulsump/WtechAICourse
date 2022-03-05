Homework Details:

Implement linear regression from scratch without using a library (do not use scikit-learn’s regression function or any other library’s regression function). 
You can use numpy, pandas, matplotlib or other helper libraries.

Details:

- First generate some data points as your input data for regression. You can use the following function or develop your own function for data generation

def generate_data(n, beta_0, beta_1):

x = np.arange(n)

e = np.random.uniform(-10,10, size=(n,))

y = beta_0 + beta_1* x + e

return x,y

i.e., you can call this function to create 100 data points (x,y)

x, y = generate_data(100, 2, .4)


- Find the line that fits best to the generated data. Use MSE (mean root square error) as your cost function.
- Plot the line you find using your regression function. You can use matplotlib  or any python plotting library.
- Plot the MSE or RMSE of your regression function during iterations.
