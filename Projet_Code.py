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
    def __init__(self,L,Beta,m,Jx,Jz):
        "private variables size & extent, weight_list, binary_chessboard, worldlines_board"
        self.Jx = Jx
        self.Jz = Jz
        self.size = L
        self.Dtau = Beta/m
        self.m = m
        self.Beta = Beta

        self.weight_list = [
            np.exp(self.Dtau*Jx/4)*np.cosh(self.Dtau*Jx/2),
            np.exp(-self.Dtau*Jx/4)*np.sinh(self.Dtau*Jx/2),
            np.exp(-self.Dtau*Jz/4)
        ]

        "create the chessboard"

        #Create an array x and y that stores all integer between 0 and L,
        x = np.arange(0, L,1)
        y = np.arange(0, m,1)
        #Limits of our chessboard
        self.extent = (np.min(x), np.max(x)+1, np.min(y), np.max(y)+1)

        #To calculate the alternate position for coloring, use the outer function,
        #which results in two vectors, and the modulus is 2.
        z1 = np.add.outer(range(2*m), range(L)) % 2

        self.binary_chessboard = z1

        "initializing the white square of the chessboard with fixed wordline configuration"
        self.worldlines_board = np.empty((2*m,L), dtype=Square)

        for j in range(L):
            for i in range(2*m):
                if (i+j)%2 == 1:
                    "if there are black square, no information is needed"
                    self.worldlines_board[i][j] = np.nan
                else:
                    "instantiating white squares"
                    if i%2 == 0 and j%2 == 0:
                        self.worldlines_board[i][j] = Square(2,self)
                    else:
                        self.worldlines_board[i][j] = Square(1,self)

        
                
    def _get_square(self,i,j):
        "give the square in i,j"
        return self.worldlines_board[i][j]

    def _get_weight(self,sqr_type):
        "give the weight of a given type, type in [1,2,3,4,5,6]"
        return self.weight_list[(sqr_type-1)//2]

    def _config_to_image(self):
        "plot the chessboard with its current wordlines"

        "adding all the worldlines to lines[]"
        config = self.worldlines_board 
        lines = []

        b,a = len(config),len(config[0])
        
        
        for j in range(0,b):
            for i in range(0,a):
                if (j+i)%2 == 0:
                    #scanning all the white square
                    #add to lines[] the corresponding segment for a given position and type of square
                    sq_t = config[j][i].square_type
                    if sq_t == 1 or sq_t == 5:
                        #vertical left line
                        lines.append([(i,j),(i,j+1)]) # TODO : maybe need to change
                    if sq_t == 2 or sq_t == 5:
                        #vertical right line
                        lines.append([(i+1,j),(i+1,j+1)])
                    if sq_t == 3:
                        #diagonal line from left to right
                        lines.append([(i+1,j),(i,j+1)])
                    if sq_t == 4:
                        #diagonal line from right to left
                        lines.append([(i,j),(i+1,j+1)])
        

        "Beginning figure"
        fig, ax = plt.subplots()

        #plotting the chessboard without the worldlines yet
        plt.imshow(self.binary_chessboard, cmap='binary_r', interpolation='nearest', extent=self.extent, alpha=1, aspect = 1)
        
        #plotting the lines in lines[]
        color_red = (1, 0, 0, 1)
        lc = mc.LineCollection(lines, colors=color_red, linewidths=4)
        ax.add_collection(lc)

        plt.show()



class Square(Chessboard):
    "Square of a chessboard defining its type and weight"
    def __init__(self, sqr_type, chess_a : Chessboard):
        self.square_type = sqr_type
        self.weight = chess_a._get_weight(sqr_type)

    def _update(self, sqr_type):
        "update the attribute of the square"
        self.square_type = sqr_type
        self.weight = Chessboard._get_weight(sqr_type)




