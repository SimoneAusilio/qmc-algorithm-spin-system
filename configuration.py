import itertools
import numpy as np
import spin


class Configuration:
    '''Represents spin configuration of the XXZ spin chain'''

    def __init__(self, chess):
        '''Initialize spin configurations'''
        self.size=chess.size+1
        self.m=chess.Beta//chess.Dtau
        self.Jx=chess.Jx
        self.Jz=chess.Jz
        self.config=np.zeros(chess.size, self.m)
        for j, i in itertools.product(range(chess.size), range(2*self.m)):
            if (i+j)%2==0 and i%2==0:  # white squares on even rows
                n=chess._get_square(i,j).square_type
                # cases
                if n==1:
                    self.config[i][j]=1
                    self.config[i][(j+1)%chess.size]=-1
                    self.config[i+1][j]=1
                    self.config[i+1][(j+1)%chess.size]=-1
                elif n==2:
                    self.config[i][j]=-1
                    self.config[i][(j+1)%chess.size]=1
                    self.config[i+1][j]=-1
                    self.config[i+1][(j+1)%chess.size]=1
                elif n==3:
                    self.config[i][j]=-1
                    self.config[i][(j+1)%chess.size]=1
                    self.config[i+1][j]=1
                    self.config[i+1][(j+1)%chess.size]=-1
                elif n==4:
                    self.config[i][j]=1
                    self.config[i][(j+1)%chess.size]=-1
                    self.config[i+1][j]=-1
                    self.config[i+1][(j+1)%chess.size]=1
                elif n==5:
                    self.config[i][j]=1
                    self.config[i][(j+1)%chess.size]=1
                    self.config[i+1][j]=1
                    self.config[i+1][(j+1)%chess.size]=1
                else:
                    self.config[i][j]=-1
                    self.config[i][(j+1)%chess.size]=-1
                    self.config[i+1][j]=-1
                    self.config[i+1][(j+1)%chess.size]=-1
        
        def get_energy(self, i):
            '''Returns the enrgy of the configuration at row j'''
            return spin.energy(self.Jx, self.Jz, self.config[i])