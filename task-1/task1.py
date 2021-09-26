import numpy as np 
import matplotlib.pylab as plt
from lagrange import plot_interpolation, w

# Parameters for the Lagrange Interpolation: interpolate in the interval [xmin, xmax], N points.
xmin = -1
xmax = 1 
N = 15   

# General Plotting Parameters    
mesh_size = 100
xplot = np.linspace(start = xmin, stop=xmax, num= mesh_size)

# Points for the EQUIDISTANT SPACING part of the question (1)
x_vals_1 = np.linspace(xmin, xmax, N)

# Points for the CHEBYCHEV SPACING (roots of T15) part of the question (2)
x_vals_2 = np.array([np.cos(np.pi*(2*j+1)/(2*N+2)) for j in range(0, N)], float)


# Question (1a): Equidistant Spacing, f(x) = sin(x)
y1 = np.sin(x_vals_1)
true_y1 = np.sin(xplot)
title1 = "Lagrange Interpolation, Equidistant Points, Sin(x)"
plot_interpolation(x_vals_1, y1, xplot, title1, true_y1)

# Question (1b): Equidistant Spacing, f(x) = Heaviside(x)
y2 = np.heaviside(x_vals_1, 1)
true_y2 = np.heaviside(xplot, 1)
title2 = "Lagrange Interpolation, Equidistant Points, Heaviside Fxn"
plot_interpolation(x_vals_1, y2, xplot, title2, true_y2)

# Question (1c): Equidistant Spacing, f(x) = 1/(10x^2 + 1)
y3 = w(x_vals_1)
true_y3 = w(xplot)
title3 = "Lagrange Interpolation, Equidistant Points, w(x) Fxn"
plot_interpolation(x_vals_1, y3, xplot, title3, true_y3)

# Question (2a): Chebychev Spacing, f(x) = sin(x)
y4 = np.sin(x_vals_2)
title4 = "Lagrange Interpolation, Chebychev Points, Sin(x)"
plot_interpolation(x_vals_2, y4, xplot, title4, true_y1)

# Question (2b): Chebychev Spacing, f(x) = Heaviside(x)
y5 = np.heaviside(x_vals_2, 1)
title5 = "Lagrange Interpolation, Chebychev Points, Heaviside"
plot_interpolation(x_vals_2, y5, xplot, title5, true_y2)

# Question (2c): Chebychev Spacing, f(x) = 1/(10x^2 + 1)
y6 = w(x_vals_2)
title6 = "Lagrange Interpolation, Chebychev Points, w(x) Fxn"
plot_interpolation(x_vals_2, y6, xplot, title6, true_y3)