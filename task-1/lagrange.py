import numpy as np 
import matplotlib.pylab as plt

# Helper Functions 
'''
Input: x0: the input for the function doing the lagrange polynomial
	   x_vals: values that we interpolate with (x)
	   y_vals: values that we interpolate with (y)
Output: y0: the predicted y value based on the interpolation.
'''
def lagrange_evaluate(x0, x_vals, y_vals):
	y0 = 0 						# initial value for y 
	for xi, yi in zip(x_vals, y_vals):
		p = 1 					# initial value of the product 
		# obtaining the ith basis polynomial:
		p = np.prod((x0 - x_vals[x_vals != xi])/(xi - x_vals[x_vals != xi]))
		# adding that basis polynomial, weighting it by the yi value
		y0 += yi * p
	return y0

'''
Input: xplot: the x-values to plot
       x_vals: values that we interpolate with (x)
       y_vals: values that we interpolate with (y)
Output: an array, yplot, with the interpolated values.
'''
def lagrange_interpolation(xplot, x_vals, y_vals):
	yplot = np.array([])
	for x0 in xplot:
		# given a value x0, what's the Lagrange interpolation y0?
		y0 = lagrange_evaluate(x0, x_vals,y_vals)

		# add this value to our array to plot.
		yplot = np.append(yplot, y0)
	return yplot

# A function to plot the interpolation
def plot_interpolation(x_vals, y_vals, xplot, title, true_function):
	yplot = lagrange_interpolation(xplot, x_vals, y_vals)
	plt.plot(x_vals, y_vals, 'ro', xplot, yplot, 'b-')
	plt.plot(xplot, true_function)
	plt.xlabel('x')
	plt.ylabel('y')
	plt.title("{}".format(title))
	plt.show()

# for the final function defined on [-1, 1]
def w_evaluate(x0):
	return (1/(10*x0**2 + 1))

def w(xplot):
	yplot = np.array([])
	for x0 in xplot:
		yplot = np.append(yplot, w_evaluate(x0))
	return yplot