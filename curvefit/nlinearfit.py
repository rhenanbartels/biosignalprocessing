import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

#Create the x and y values
xdata = np.linspace(0, 10, 200)
ydata = 10 + 15 * np.exp(-xdata / 2) + np.random.randn(len(xdata))


#Define the exponential model
def my_fun(par, t, y):
    err = y - (par[0] + par[1] * np.exp(-t / par[2]))
    return err


#Function to evaluate the model
def fun_eval(par, t):
    return par[0] + par[1] * np.exp(-t / par[2])

#Initial guests
p0 = [min(ydata), max(ydata) - min(ydata), xdata[-3] / 3]

#Nonlinear fit
result = leastsq(my_fun, p0, args=(xdata, ydata))

#Plot the curves
plt.plot(xdata, ydata, 'k.')
plt.plot(xdata, fun_eval(result[0], xdata), 'r')
plt.xlabel("Time (s)")
plt.ylabel("Signal")
plt.show()
