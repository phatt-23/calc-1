import numpy as np
import matplotlib.pyplot as plt

def f(x):
    term1 = 2 * x**6
    term2 = -3 * x**2 / np.cbrt(x)
    term3 = -7 * np.sin(x)
    term4 = 2 / (x**2 + 1)
    term5 = 11 / x
    return term1 + term2 + term3 + term4 + term5

def F(x):
    term1 = (2 * x**7) / 7
    term2 = - (9 * np.cbrt(x**8)) / 8
    term3 = 7 * np.cos(x)
    term4 = 2 * np.arctan(x)
    term5 = 11 * np.log(np.abs(x))
    return term1 + term2 + term3 + term4 + term5

x_values1_neg = np.linspace(-2.5,-0.01,1000)
x_values1_pos = np.linspace(0.01,2.5,1000)
y_values1_neg = f(x_values1_neg)
y_values1_pos = f(x_values1_pos)
x_values2 = np.linspace(-2.5,2.5,1000)
y_values2 = F(x_values2)

np.savetxt("plot_data1_neg.txt", np.column_stack((x_values1_neg, y_values1_neg)))
np.savetxt("plot_data1_pos.txt", np.column_stack((x_values1_pos, y_values1_pos)))
np.savetxt("plot_data2.txt", np.column_stack((x_values2, y_values2)))
