#Importing modules (numpy, and matplotlib.pyplot)
import numpy as np
import matplotlib.pyplot as pyplot

L = 8
Beta = 20
Dtau = 2
#Declare the size of the interval dx, dy.
(dx, dy) = (1, 1)

#Create an array x and y that stores all values with dx and dy intervals,
#arange() is a NumPy library function
#that gives an array of objects with equally spaced values within a defined interval.
x = np.arange(0, L*dx,dx)
y = np.arange(0, Beta/Dtau*dy,dy)

#Plot a rectangle grid with vector coordinates.
(X, Y) = np.meshgrid(x, y)
extent = (np.min(x), np.max(x)+1, np.min(y), np.max(y)+1)


#To calculate the alternate position for coloring, use the outer function,
#which results in two vectors, and the modulus is 2.
z1 = np.add.outer(range(int(Beta/Dtau)), range(L)) % 2

pyplot.imshow(z1, cmap='binary_r', interpolation='nearest', extent=extent, alpha=1, aspect = 1)

#set the plot's title.
pyplot.title('Chess Board')

# Save the chart file
#pyplot.savefig('matplotlib_pie_chart01.png', dpi=300)

# Print the chart
pyplot.show()