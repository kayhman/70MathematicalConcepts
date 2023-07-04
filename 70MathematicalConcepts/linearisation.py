import numpy as np
import matplotlib.pyplot as plt

# This function creates a linearized
# function for f at the point $x_0$.
def linearise(f, f_p, x_0):
    f_lin = lambda x: f(x_0) + f_p(x_0) * (x - x_0)
    return f_lin


f = lambda x: x**2 # x² is the function to be linearized
f_p = lambda x: 2*x # 2x is the derivative of f(x)
x_0 = 1.0 # $x_0$ is the point of linearization
f_lin = lambda x: linearise(f, f_p, x_0)(x) # f\_lin(x) is the linearization of f(x) at the point $x_0$

xs = np.linspace(-3, 3, 100)
ys = [f(x) for x in xs]
xs2 = np.linspace(0, 3, 100)
f_lin_x_1 = [f_lin(x) for x in xs2]
plt.plot(xs, ys, xs2, f_lin_x_1, '-.',
         [x_0], f(x_0), 'o')
plt.show()
