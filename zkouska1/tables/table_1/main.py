import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x**2019 + np.sin(2019*x))/(np.exp(2019*x)-x-1)

x_values = np.linspace(-0.005,0.005,1000)
y_values = f(x_values)

np.savetxt('plot_data.txt', np.column_stack((x_values, y_values)))
