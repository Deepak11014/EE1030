# Code by GVV Sharma
# Modified for Problem Solution
# Released under GNU GPL
# Calculating area enclosed between curves
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.optimize import fsolve

import sys  # For path to external scripts
sys.path.insert(0, '/home/deepak/EE1030/matgeo/codes/CoordGeo')  # Path to my scripts

# Read the values from the C-generated text file using numpy.loadtxt
data = np.loadtxt('data.txt')

# Extracting parabola and circle parameters
p = data[0]  # Parabola parameter (x^2 = 4py)
r = data[1]  # Circle radius
h = data[2]  # Circle center x-coordinate
k = data[3]  # Circle center y-coordinate

# Parabola equation: x^2 = 4py, so y = x^2 / (4p)
def parabola(x, p):
    return x**2 / (4 * p)

# Circle equation: (x - h)^2 + (y - k)^2 = r^2, so y = k + sqrt(r^2 - (x - h)^2)
def circle(x, r, h, k):
    return k + np.sqrt(r**2 - (x - h)**2)

# Find the points of intersection between the parabola and the circle
def find_intersections(p, r, h, k):
    def intersection_eq(x):
        return circle(x, r, h, k) - parabola(x, p)

    x_int1 = fsolve(intersection_eq, -r)[0]
    x_int2 = fsolve(intersection_eq, r)[0]

    return x_int1, x_int2

# Get the intersection points
x_int1, x_int2 = find_intersections(p, r, h, k)

# Compute the area between the curves using integration
def area_between_curves(x, p, r, h, k):
    return circle(x, r, h, k) - parabola(x, p)

# Perform the integration from x_int1 to x_int2
area, _ = quad(area_between_curves, x_int1, x_int2, args=(p, r, h, k))

print(f"Area enclosed between the parabola and the circle: {area}")

# Visualization

# Generating points for the parabola and circle
x_vals = np.linspace(-r, r, 400)
y_parabola = parabola(x_vals, p)
y_circle_upper = circle(x_vals, r, h, k)

# Generate the lower half of the circle
y_circle_lower = k - np.sqrt(r**2 - (x_vals - h)**2)

# Plot the curves
plt.plot(x_vals, y_parabola, label=r'Parabola: $x^2 = 4py$', color='r')
plt.plot(x_vals, y_circle_upper, label=r'Circle: $(x - %.2f)^2 + (y - %.2f)^2 = %.2f^2$' % (h, k, r), color='b')
plt.plot(x_vals, y_circle_lower, color='b')  # Lower part of the circle (no extra label)

# Fill the area between the curves
plt.fill_between(x_vals, y_parabola, y_circle_upper, where=(y_circle_upper >= y_parabola), color='lightblue', alpha=0.5)

# Labels and plot settings
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Area Enclosed by the Parabola and Circle')
plt.grid(True)
plt.legend()

# Set equal aspect ratio to avoid distortion
plt.gca().set_aspect('equal', adjustable='box')

# Show the plot
plt.show()

