import itertools
import numpy as np
import spin


class Configuration:
    '''Represents spin configuration of the XXZ spin chain'''

    def __init__(self, chess):
        '''Initialize spin configurations'''
        self.size=chess.size+1
        self.Jx=chess.Jx
        self.Jz=chess.Jz
        self.m=chess.m
        self.config=np.zeros((2*self.m, self.size), dtype=int)
        # iteration over of rows from the bottom
        for i in range(2*self.m-1, -1, -1):
            # iteration over columns of the square
            for j in range(chess.size):
                if (i+j)%2==1:  # positions of white squares
                    n=chess.worldlines_board[i][j].square_type
                    # cases (same order from fig. 10.1 of the chapter)
                    if n==1:
                        self.config[i][j]=+1
                        self.config[i][j+1]=-1
                        self.config[(i+1)%(2*self.m)][j]=+1
                        self.config[(i+1)%(2*self.m)][j+1]=-1
                    elif n==2:
                        self.config[i][j]=-1
                        self.config[i][j+1]=+1
                        self.config[(i+1)%(2*self.m)][j]=-1
                        self.config[(i+1)%(2*self.m)][j+1]=+1
                    elif n==3:
                        self.config[i][j]=-1
                        self.config[i][j+1]=+1
                        self.config[(i+1)%(2*self.m)][j]=+1
                        self.config[(i+1)%(2*self.m)][j+1]=-1
                    elif n==4:
                        self.config[i][j]=+1
                        self.config[i][j+1]=-1
                        self.config[(i+1)%(2*self.m)][j]=-1
                        self.config[(i+1)%(2*self.m)][j+1]=+1
                    elif n==5:
                        self.config[i][j]=+1
                        self.config[i][j+1]=+1
                        self.config[(i+1)%(2*self.m)][j]=+1
                        self.config[(i+1)%(2*self.m)][j+1]=+1
                    elif n==6:
                        self.config[i][j]=-1
                        self.config[i][j+1]=-1
                        self.config[(i+1)%(2*self.m)][j]=-1
                        self.config[(i+1)%(2*self.m)][j+1]=-1

    def get_energy(self, i):
        '''Returns the enrgy of the configuration at row i'''
        return spin.energy(self, i)