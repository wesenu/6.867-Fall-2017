import numpy as np
from loadFittingDataP1 import getData
from q1 import batch_gradient_descent
import random
import matplotlib.pyplot as plt
# Batch Gradient Descent

def loss_function(X, y):
    def loss_function_sampler(theta):
        ideal = np.dot(X, theta)
        loss = ideal - y
        loss_squared = np.square(loss)
        loss_sum = np.sum(loss_squared)
        return loss_sum*0.5
    return loss_function_sampler

def loss_function_der(X, y):
    def loss_function_der_sampler(theta):
        loss = np.dot(X, theta) - y
        return np.dot(np.transpose(X),loss)
    return loss_function_der_sampler


def learning_rate(a, b):
    assert a >= 0
    assert b > 0.5
    assert b < 1.0
    def learning_rate_sampler(t):
        return (a + t) ** -b
    return learning_rate_sampler



data = getData()

X = data[0]

y = data[1]

init = np.ones(10)

func_loss = loss_function(X, y)
func_loss_der = loss_function_der(X, y)

# value, steps = batch_gradient_descent(init, 1e-7, 1e-8, func_loss, func_loss_der, True)
# print "Theta for BGD: ", value
# print "Iterations: ", steps

# plt.plot(store_steps, store_grads)
# plt.ylabel("Magnitude of Gradient")
# plt.xlabel("Number of iterations")
# plt.title("Batch Gradient Descent")
# plt.show()


print y.size


# Stochastic Gradient Descent







average_theta = np.zeros(10)
average_iterations = 0
average_error = 0

store_sgd_steps = []
store_sgd_grads = []

for i in xrange(10):
    X_0 = np.copy(X[0])
    X_0.shape = (1, 10)
    y_0 = np.array([np.copy(y[0])])

    stochastic_loss = loss_function(X_0, y_0)
    stochastic_loss_der = loss_function_der(X_0, y_0)
    step_function = learning_rate(1e7, 0.9)

    current_value = np.ones(10)
    gradient = stochastic_loss_der(current_value)
    iteration = 0
    epsilon = 1e-3

    while np.linalg.norm(gradient) > epsilon:

        i = random.randint(0,99)

        X_i = np.copy(X[i])
        X_i.shape = (1,10)
        y_i = np.array([np.copy(y[i])])

        stochastic_loss = loss_function(X_i, y_i)
        stochastic_loss_der = loss_function_der(X_i, y_i)

        current_value -= step_function(iteration) * gradient
        gradient = stochastic_loss_der(current_value)
        # maybe ???
        if i == 0 and len(store_sgd_steps) < 200:

            store_sgd_grads.append(np.linalg.norm(gradient))
            store_sgd_steps.append(iteration)

        iteration += 1





    average_theta += current_value
    average_iterations += iteration

    #store_sgd_steps.append(average_iterations/10)
    average_error += func_loss(current_value)

average_theta = average_theta / 10.0
average_iterations = average_iterations / 10.0
average_error = average_error / 10.0

plt.scatter(store_sgd_steps, store_sgd_grads)
plt.ylabel("Magnitude of Gradient")
plt.xlabel("Number of iterations")
plt.title("Stochastic Gradient Descent")
plt.show()


print "Theta for SGD: ", average_theta
print "Iterations: ", average_iterations
#print "Average error function: ", average_error
