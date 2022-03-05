import matplotlib.pyplot as plt
import numpy as np 

#The fuction create dataset that contains points (x,y)
def generate_data(n,beta_0,beta_1):
     
    # n = number of data points
    x = np.arange(n)
    e = np.random.uniform(-10,10, size=(n,))

    #beta_0 = bias value
    #beta_1= weight  value
    
    y = beta_0 + beta_1* x + e
    
    return x,y

   

#Create some data points
x , y = generate_data (100,2,.4)

#This values was determined by ours

#weight= slope of line
weight=0.9

# bias = intercept so the value of y when x=0
bias=3

#epochs = number of iterations
epochs=50

#learning_rate = Coefficient of Gradient Descent Steps
learning_rate=0.000002


#The fuction apply Linear Regression algorithm and returns weight,bias,cost
#Calculates Mean Square Error as Cost Function
#Calculates Gradient Descent

def linear_regression(x, y, weight, bias, learning_rate):
    #N=total number
    N = float(len(y))
    
    weight_derivative = 0
    bias_derivative = 0
    sum_error=0


    for i in range(int(N)):
        
        #calculate prediction of y value
        predict_y = (weight * x[i]) + bias

        #Calculate total error
        sum_error += (predict_y-y[i])**2

        #Calculate bias derivative and weight derivative
      
        bias_derivative = bias_derivative + (-2*(y[i]-(bias+x[i]*weight)))
        weight_derivative = weight_derivative +(-2*x[i]*(y[i]-(bias+x[i]*weight)))

    #Calculate weight and bias values from Gradient descent
    
    weight =weight - (learning_rate * weight_derivative )
    bias = bias - (learning_rate * bias_derivative)

    #calculate Mean Square Error(MSE) as cost function
    cost = sum_error / N
    
    return weight,bias,cost


#This fuction plot regression line

def plot_line(x, y, weight, bias, epochs, learning_rate):

    for i in range(epochs):
        weight , bias ,cost =linear_regression(x, y, weight, bias, learning_rate)


        #plot Linear Regression Line and Data Points end of the iterations

        if i==epochs-1:
            y1 = weight*x + bias
            plt.title('DATA POINTS & REGRESSION LINE')

            plt.scatter(x, y, color='#ef5423', label='Data Points')
            plt.plot(x, y1, color='#58b970', label='Regression Line')
    
            plt.xlabel('INDEPENDENT VALUES')
            plt.ylabel('DEPENDENT VALUES')
            plt.legend()
            plt.show()
            


#Plot Best Fit Regression Line
            
plot_line(x,y,weight,bias,epochs,learning_rate )


#Calculates the necessary parameters for plotting the MSE from iterations
    
def plot_MSE(x, y, weight, bias, epochs, learning_rate):
    cost_h = list()
    iteration_num = list()
    
    for i in range(epochs):
        weight , bias ,cost =linear_regression(x, y, weight, bias, learning_rate)

        #Add values for some iteration interval 
        if i % 10 == 0 :
            iteration_num.append(i)
            cost_h.append(cost)
        
    return cost_h,iteration_num


# return cost_h and iteration_num for plotting MSE

MSE , iterations = plot_MSE(x,y,weight,bias,epochs,learning_rate)

#Plot the MSE of own regression function during iterations.
plt.title('MSE as a Cost Function')
plt.plot(iterations, MSE , color='#58b970', label='MSE LİNE' )
plt.xlabel('Number of Iterations')
plt.ylabel('Mean  Square Error')
plt.legend()
plt.show()

