import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections  as mc 
import Projet_Code
import configuration

L=np.arange(2, 11)
m=np.arange(2, 11)
Jx=1
Jz=2
beta=np.arange(0, 50)

'''
# data collection
length_cycle=100    # number of update trials (arbitrary for the moment)
n_warmup=100    # number of simulations made at the beginning
n_cycles=100    # number of measurements

beta_range=np.arange()
chess=Projet_Code.Chessboard(L, Beta, m, Jx, Jz)
conf=configuration.Configuration(chess)'''