# plot_2d.py
# func for plotting 2d quadratics and making contours
# Author: T Weihing
# Date: 6/29/2019

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# -----------------------------------------------
# Equation: A*x1**2 + B*x1*x2 + C*x2**2 + D*x1 + E*x2 + F
# -----------------------------------------------

# -----------------------------------------------
# Inputs:

plotSurface = True
plotContours = True

A = 2
B = 2
C = 1
D = -1
E = 2
F = 0

# -----------------------------------------------
# Function calcs:
x1 = np.linspace(-2, 2, 100)
x2 = np.linspace(-2, 2, 100)
x1x2_quadratic = np.zeros([100,100])


for x1_idx in range(len(x1)):
    for x2_idx in range(len(x2)):
        x1x2_quadratic[x2_idx][x1_idx] = A*x1[x1_idx]**2 + B*x1[x1_idx]*x2[x2_idx] + C*x2[x2_idx]**2 + D*x1[x1_idx] + E*x2[x2_idx] + F
        # For whatever reason, Z in contourf is Z(y,x) instead of z(x,y)


#print(type(xy_quadratic[1][1]))
print(x1x2_quadratic)

# -----------------------------------------------
# Plotting:

fig, ax = plt.subplots()
cs = plt.contourf(x1, x2, x1x2_quadratic)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
plt.show()