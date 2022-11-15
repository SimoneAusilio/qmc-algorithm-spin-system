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
        self.config=np.zeros((2*self.m, self.size))
        for i in range(self.m):
            k=self.m-1-i
            for j in range(chess.size):
                if (k+j)%2==0:
                    n=chess._get_square(k, j)
                    # cases
                    if n==1:
                        self.config[2*k][j]=1
                        self.config[2*k][j+1]=-1
                        self.config[2*k+1][j]=1
                        self.config[2*k+1][(j+1)%self.size]=-1
                    elif n==2:
                        self.config[2*k][j]=-1
                        self.config[2*k][(j+1)%self.size]=1
                        self.config[2*k+1][j]=-1
                        self.config[2*k+1][(j+1)%self.size]=1
                    elif n==3:
                        self.config[2*k][j]=-1
                        self.config[2*k][(j+1)%self.size]=1
                        self.config[2*k+1][j]=1
                        self.config[2*k+1][(j+1)%self.size]=-1
                    elif n==4:
                        self.config[2*k][j]=1
                        self.config[2*k][(j+1)%self.size]=-1
                        self.config[2*k+1][j]=-1
                        self.config[2*k+1][(j+1)%self.size]=1
                    elif n==5:
                        self.config[2*k][j]=1
                        self.config[2*k][(j+1)%self.size]=1
                        self.config[2*k+1][j]=1
                        self.config[2*k+1][(j+1)%self.size]=1
                    else:
                        self.config[2*k][j]=-1
                        self.config[2*k][(j+1)%self.size]=-1
                        self.config[2*k+1][j]=-1
                        self.config[2*k+1][(j+1)%self.size]=-1
        
        def get_energy(self, i):
            '''Returns the enrgy of the configuration at row j'''
            return spin.energy(self.Jx, self.Jz, self.config[i])