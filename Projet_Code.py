import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections  as mc 
from random import *
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
                if (i+j)%2 == 0:
                    "if there are black square, no information is needed"
                    self.worldlines_board[i][j] = np.nan
                else:
                    "instantiating white squares"
                    if i%2 == 1 and j%2 == 0:
                        self.worldlines_board[i][j] = Square(2,self)
                    else:
                        self.worldlines_board[i][j] = Square(1,self)

        
                
    def _get_square(self,i,j):
        "give the square in i,j"
        return self.worldlines_board[i][j]

    def _get_weight(self,sqr_type):
        "give the weight of a given type, type in [1,2,3,4,5,6]"
        return self.weight_list[(sqr_type-1)//2]

    def _get_config(self):
        return self.worldlines_board

    def _config_to_image(self):
        "plot the chessboard with its current wordlines"

        "adding all the worldlines to lines[]"
        config = self.worldlines_board 
        lines = []

        b,a = len(config),len(config[0])
        
        
        for j in range(0,b):
            for i in range(0,a):
                if (j+i)%2 == 1:
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
    
    def local_update(self):
        "effectuate one step of the local_update algorithme"
        "choose uniformly a black square among the available ones for an update"
        "Use a metropolis rules to choose wether or not a change should happened"
        config = self.worldlines_board
        L = self.size
        m = self.m

        "reportering the possible black square for a local update"
        possible_update = []
        for j in range(0,L-2,2):
            for i in range(0,m-2,2):
                left_c = config[i][j]._get_square_type()
                if left_c == 5 or left_c == 2:
                    right_c = config [i][j+2]._get_square_type()
                    if right_c == 2 or right_c == 6:
                        possible_update.append([i,j+1,left_c,right_c])
        print("phase 1")
        "Draw one at random and see if it is accepted"
        #left,right,up,down_c are the old configurations, Left, Right,Up,Down_c are the new"
        random_draw = randint(0,len(possible_update)-1)
        i,j,left_c,right_c = possible_update[random_draw]
        up_c = config[i+1,j]._get_square_type()
        down_c = config[i-1,j]._get_square_type()
        print("phase 2")
        # computing the new conf
        if left_c == 5: Left_c = 1
        else : Left_c = 6
        if right_c == 2 : Right_c = 5
        else : Right_c = 1
        if up_c == 1 : Up_c = 3
        else : Up_c = 2
        if down_c == 1 : Down_c = 4
        else : Down_c = 2
        print(left_c,Left_c)
        #computing DeltaE
        W_i = 0
        W_f = 0
        for k in [left_c,right_c,up_c,down_c]:
            W_i += self._get_weight(k)
        for k in [Left_c,Right_c,Up_c,Down_c]:
            W_f += self._get_weight(k)
        Delta_W = W_f/W_i
        print(Delta_W)
        "Do the change if it was accepted"
        #metropolis accepting protocol and changing conf
        if Delta_W >= random():
            print("phase 5")
            config[i-1][j] = Square(Down_c,self)
            config[i+1][j] = Square(Up_c,self)
            config[i][j-1] = Square(Left_c,self)
            config[i][j+1] = Square(Right_c,self)  

        #return new energy?           



class Square(Chessboard):
    "Square of a chessboard defining its type and weight"
    def __init__(self, sqr_type, chess_a : Chessboard):
        self.square_type = sqr_type
        self.weight = chess_a._get_weight(sqr_type)

    def _update(self, sqr_type):
        "update the attribute of the square"
        self.square_type = sqr_type
        self.weight = Chessboard._get_weight(sqr_type)
    
    def _get_square_type(self):
        return self.square_type




