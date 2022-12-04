import numpy as np
import square
import vertex
import numpy.random as rnd
from Projet_Code import Chessboard

L=2
Beta=20
m=1
Jx=1
Jz=2
chess=Chessboard(L, Beta, m, Jx, Jz)
chess._plot_chessboard_image()
vertex.loop(chess)
chess._plot_chessboard_image()