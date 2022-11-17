#Importing modules (numpy, and matplotlib.plt)
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections  as mc

L = 8
Beta = 20
Dtau = 2
z1 = np.add.outer(range(2*5), range(5)) % 2
z1[9][4] = 0
#plt.imshow(z1, cmap='binary_r', interpolation='nearest', extent=[0,5,0,10], alpha=1, aspect = 1)
print(z1)
plt.show()
def Print_Chessboard(L,Beta,Dtau):
    #Declare the size of the interval dx, dy.
    (dx, dy) = (1, 1)

    #Create an array x and y that stores all values with dx and dy intervals,
    #arange() is a NumPy library function
    #that gives an array of objects with equally spaced values within a defined interval.
    x = np.arange(0, L*dx,dx)
    y = np.arange(0, Beta/Dtau*dy,dy)

    extent = (np.min(x), np.max(x)+1, np.min(y), np.max(y)+1)


    #To calculate the alternate position for coloring, use the outer function,
    #which results in two vectors, and the modulus is 2.
    z1 = np.add.outer(range(int(Beta/Dtau)), range(L)) % 2

    plt.imshow(z1, cmap='binary_r', interpolation='nearest', extent=extent, alpha=1, aspect = 1)

"début de la figure"
fig, ax = plt.subplots()
Print_Chessboard(L,Beta,Dtau)

def init_config():
    "initializing a chessboard"
    chessboard = np.empty((Beta//Dtau,L))

    for j in range(L):
        for i in range(Beta//Dtau):
            if (i+j)%2 == 1:
                "if there are black square, no information is needed"
                chessboard[i][j] = np.nan
            else:
                "instantiating white squares"
                if i%2 == 0 and j%2 == 0:
                    chessboard[i][j] = 2
                else:
                    chessboard[i][j] = 1
    return chessboard

def update(config):
    "ajout des world line à la figure"
    lines = []

    b,a = len(config),len(config[0])
    c = (1, 0, 0, 1)

    for j in range(0,b):
        for i in range(0,a):
            if (j+i)%2 == 0:
                type = config[j][i]
                if type == 1 or type == 5:
                    lines.append([(i,j),(i,j+1)])
                if type == 2 or type == 5:
                    lines.append([(i+1,j),(i+1,j+1)])
                if type == 3:
                    lines.append([(i+1,j),(i,j+1)])
                if type == 4:
                    lines.append([(i,j),(i+1,j+1)])
            

    lc = mc.LineCollection(lines, colors=c, linewidths=4)
    ax.add_collection(lc)

#update(init_config())

# ax.autoscale()
# ax.margins(0.1)
plt.show()


