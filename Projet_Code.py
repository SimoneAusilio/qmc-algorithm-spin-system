import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections  as mc 
from random import *
from square import Square
import configuration

class Chessboard():
    "A Chessboard with worldlines"
    def __init__(self,L,Beta,m,Jx,Jz):
        "private variables size & extent, weight_list, binary_chessboard, worldsquare_board, worldlines_board"
        self.Jx = Jx
        self.Jz = Jz
        self.size = L
        if L%2 == 1 : 
            self.size = L+1
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
        #x = np.arange(0, L,1)
        #y = np.arange(0, m,1)
        #Limits of our chessboard
        #self.extent = (np.min(x), np.max(x)+1, np.min(y), 2*(np.max(y)+1))
        self.extent = [0,L,2*m,0]

        #To calculate the alternate position for coloring, use the outer function,
        #which results in two vectors, and the modulus is 2.
        z1 = np.add.outer(range(2*m), range(L)) % 2
        self.binary_chessboard = z1
        
        "initializing the white square of the chessboard with fixed wordline configuration"
        self.worldsquare_board = np.empty((2*m,L), dtype=Square)

        for j in range(L):
            for i in range(2*m):
                if (i+j)%2 == 0:
                    "if there are black square, no information is needed"
                    self.worldsquare_board[i][j] = np.nan
                else:
                    "instantiating white squares"
                    if j%2 == 0:
                        self.worldsquare_board[i][j] = Square(2)
                    else:
                        self.worldsquare_board[i][j] = Square(1)

        "initializing the lines of the worldboard"
        self.worldlines_board = self._get_worldlines_board()

        self.average_energy = self._get_average_energy()

        
                
    def _get_square(self,i,j):
        "give the square in i,j"
        return self.worldsquare_board[i][j]

    def _get_weight(self,sqr_type):
        "give the weight of a given type, type in [1,2,3,4,5,6]"
        return self.weight_list[(sqr_type-1)//2]

    def _get_config(self):
        return self.worldsquare_board
        
    def _get_average_energy(self):
        conf=configuration.Configuration(self)
        return np.average(np.array([conf._get_energy(i) for i in range(2*conf.m)]))/conf.size

    def _get_worldlines_board(self):
        "return a liste line with all the worldlines in it"
        config = self.worldsquare_board 
        lines = []

        b,a = len(config),len(config[0])
        
        
        for j in range(0,b):
            for i in range(0,a):
                if (j+i)%2 == 1:
                    #scanning all the white square
                    #add to lines[] the corresponding segment for a given position and type of square
                    sq_t = config[j][i]._get_square_type()
                    if sq_t == 1 or sq_t == 5:
                        #vertical left line
                        lines.append([(i,j),(i,(j+1))]) # TODO : maybe need to change
                    if sq_t == 2 or sq_t == 5:
                        #vertical right line
                        lines.append([(i+1,j),(i+1,j+1)])
                    if sq_t == 3:
                        #diagonal line from left to right
                        lines.append([(i+1,j),(i,j+1)])
                    if sq_t == 4:
                        #diagonal line from right to left
                        lines.append([(i,j),(i+1,j+1)])
        
        return lines
        
    def _plot_chessboard_image(self):
        "plot the chessboard with its current wordlines"
        "Beginning figure"
        fig, ax = plt.subplots()

        #plotting the chessboard without the worldlines yet
        plt.imshow(self.binary_chessboard, cmap='binary_r', interpolation='nearest', extent=self.extent, alpha=1, aspect=1)
        
        #getting and plotting the lines in lines[]
        color_red = (1, 0, 0, 1)
        lines = self.worldlines_board

        lc = mc.LineCollection(lines, colors=color_red, linewidths=4)
        ax.add_collection(lc)
        ax.xaxis.tick_top()

        plt.show()

    def local_update(self):
        "effectuate one step of the local_update algorithme"
        "choose uniformly a black square among the available ones for an update"
        "Use a metropolis rules to choose wether or not a change should happened"
        config = self.worldsquare_board
        L = self.size
        m = self.m

        "reportering the possible black square for a local update"
        possible_update = []
        for i in range(0,2*m):
            for j in range(0,L):
                "we look for each white square which will if it is type 1, 2 or 5"
                "if it is it will be the left square of the black square we are going to change around"
                if (i+j)%2 == 1:
                    left_c = config[i][j]._get_square_type()
                    if left_c == 5 or left_c == 2:
                        "if the left square already has a wordline on its right we look to see if the next"
                        "white doesn't have one on its left"
                        right_c = config [i][(j+2)%L]._get_square_type()
                        if right_c == 2 or right_c == 6:
                            possible_update.append([i,(j+1)%L,left_c,right_c])
                    if left_c == 1 : 
                        right_c = config [i][(j+2)%L]._get_square_type()
                        if right_c == 5 or right_c == 1 : 
                            "if the left square does not have a wordline on its right we look to see if "
                            "the next white has one on its left"
                            possible_update.append([i,(j+1)%L,left_c,right_c])
                

        "Draw one at random and see if it is accepted"
        #left,right,up,down_c are the old configurations, Left, Right,Up,Down_c are the new"
        if len(possible_update) == 0  : 
            print("stationary state")
            return None
        random_draw = randint(0,len(possible_update)-1)
        i,j,left_c,right_c = possible_update[random_draw]
        up_c = config[(i-1)%(2*m),j]._get_square_type()
        down_c = config[(i+1)%(2*m),j]._get_square_type()
        
        #computing the new configuration"
        if left_c == 5: Left_c = 1
        elif left_c == 2: Left_c = 6
        else :Left_c = 5
        if right_c == 2 : Right_c = 5
        elif right_c == 6 : Right_c = 1
        elif right_c == 5 : Right_c = 2
        else : Right_c = 6
        if up_c == 1 : Up_c = 4
        elif up_c == 3 : Up_c = 2
        elif up_c == 2 : Up_c = 3
        elif up_c == 4 : Up_c = 1
        else : Up_c = 2
        if down_c == 1 : Down_c = 3
        elif down_c == 4 : Down_c = 2
        elif down_c  == 2 : Down_c = 4
        else : Down_c = 1
        
        #computing DeltaE
        W_i = 0
        W_f = 0
        for k in [left_c,right_c,up_c,down_c]:
            W_i += self._get_weight(k)
        for k in [Left_c,Right_c,Up_c,Down_c]:
            W_f += self._get_weight(k)
        Delta_W = W_f/W_i
        
        "Do the change if it was accepted"
        #metropolis accepting protocol and changing conf on the worldsquare_board
        if Delta_W >= random():
            self.worldsquare_board[(i+1)%(2*m)][j]._update(Down_c)
            self.worldsquare_board[(i-1)%(2*m)][j]._update(Up_c)
            self.worldsquare_board[i][j-1]._update(Left_c)
            self.worldsquare_board[i][(j+1)%L]._update(Right_c)
            
            "registring the update"
            self.worldlines_board = self._get_worldlines_board()
            return True
            
        else :
            return None

        #compute new energy?           








