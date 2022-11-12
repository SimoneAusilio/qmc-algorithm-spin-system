import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections  as mc
# class Mother_Square:
#     "Abstract Square saving the various weight"
#     def __init__(self,Dtau,Jx,Jz):
#         self.weight_list = [
#             np.exp(Dtau*Jx/4)*np.cosh(Dtau*Jx/2),
#             np.exp(-Dtau*Jx/4)*np.sinh(Dtau*Jx/2),
#             np.exp(-Dtau*Jz/4)
#         ]
    
#     def _get_weight(self,type):
#         return self.weight_list[type//2]

class Chessboard:
    "A Chessboard with worldlines"
    def __init__(self,L,Beta,Dtau,Jx,Jz):
        self.size = L
        self.weight_list = [
            np.exp(Dtau*Jx/4)*np.cosh(Dtau*Jx/2),
            np.exp(-Dtau*Jx/4)*np.sinh(Dtau*Jx/2),
            np.exp(-Dtau*Jz/4)
        ]

        "initializing a chessboard"
        self.chessboard = np.empty((Beta//Dtau,L))

        for i in range(L):
            for j in range(Beta/Dtau):
                if (i+j)%2 == 1:
                    "if there are black square, no information is needed"
                    self.chessboard[i][j] = np.nan
                else:
                    "instantiating white squares"
                    if i%2 == 0 and j%2 == 0:
                        self.chessboard[i][j] = Square(2)
                    else:
                        self.chessboard[i][j] = Square(1)
                
    def _get_square(self,i,j):
        "give the square in i,j"
        return self.chessboard[i][j]

    def _get_weight(self,type):
        "give the weight of a given type, type in [1,2,3,4,5,6]"
        return self.weight_list[(type-1)//2]

    def _config_to_image(self):
        config = self.chessboard 
        
class Graphic_Chessboard(Chessboard):
    "create a chessboard of given dimentions"
    def __init__(self,L,Beta,Dtau):
        "create the chessboard"
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

        self.binary_chessboard = z1
        
    
    def _update(self,config):
        lines = []

        b,a = len(config),len(config[0])
        c = (1, 0, 0, 1)

        for j in range(0,b,2):
            for i in range(0,a,2):
                type = config(i,j)
                if type == 1 or type == 5:
                    lines.append([(i,j),(i,j+1)])
                if type == 2 or type == 5:
                    lines.append([(i+1,j),(i+1,j+1)])
                if type == 3:
                    lines.append([(i+1,j),(i,j+1)])
                if type == 4:
                    lines.append([(i,j),(i+1,j+1)])
                

        lc = mc.LineCollection(lines, colors=c, linewidths=2)
        


    def _show(self):
        
        plt.show()



class Square(Chessboard):
    "Square of a chessboard defining its type and weight"
    def __init__(self,type):
        self.type = type
        self.weight = Chessboard._get_weight(type)

    def _update(self,type):
        "update the attribute of the square"
        self.type = type
        self.weight = Chessboard._get_weight(type)






