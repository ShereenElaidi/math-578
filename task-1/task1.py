import numpy as np 
import matplotlib.pylab as plt
from lagrange import plot_interpolation, w

xmin = -1
xmax = 1 
N = 15       # number of data points
mesh_size = 100
xplot = np.linspace(start = xmin, stop=xmax, num= mesh_size)
x_vals_1 = np.linspace(xmin, xmax, N)


y_vals1 = np.sin(x_vals_1)
true_y1 = np.sin(xplot)
title1 = "Lagrange Interpolation, Equidistant Points, Sin(x)"
# plot_interpolation(x_vals_1, y_vals1, xplot, title1, true_y1)


y_vals2 = np.heaviside(x_vals_1, 1)
true_y2 = np.heaviside(xplot, 1)
title2 = "Lagrange Interpolation, Equidistant Points, Heaviside Fxn"
# plot_interpolation(x_vals_1, y_vals2, xplot, title2, true_y2)

y_vals3 = w(x_vals_1)
true_y3 = w(xplot)
title3 = "Lagrange Interpolation, Equidistant Points, w(x) Fxn"
# plot_interpolation(x_vals_1, y_vals3, xplot, title3, true_y3)

# now for interpolating chebychev points; we want our x_vals to be the roots of
# T15, the 15th Chebyshev Polynomial

x_vals_2 = np.array([np.cos(np.pi*(2*j+1)/(2*N+2)) for j in range(0, N)], float)
y_vals_4 = np.sin(x_vals_2)
title4 = "Lagrange Interpolation, Chebychev Points, Sin(x)"
plot_interpolation(x_vals_2, y_vals_4, xplot, title4, true_y1)

y_vals_5 = np.heaviside(x_vals_2, 1)
title4 = "Lagrange Interpolation, Chebychev Points, Heaviside"
plot_interpolation(x_vals_2, y_vals_5, xplot, title4, true_y2)

y_vals_5 = w(x_vals_2)
title5 = "Lagrange Interpolation, Chebychev Points, w(x) Fxn"
plot_interpolation(x_vals_2, y_vals_5, xplot, title5, true_y3)



