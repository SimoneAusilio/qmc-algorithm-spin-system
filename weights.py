import numpy as np
from square import Square

def prob(sq: Square, g: int, Dtau: float, Jx: float, Jz: float):
    '''Returns the probability of an allowed breakup on a vertex (<->square type)'''
    n=sq._get_square_type()
    # weights of vertices
    w1=np.exp(Dtau*Jx/4)*np.cosh(Dtau*Jx/2)
    w2=np.exp(-Dtau*Jx/4)*np.sinh(Dtau*Jx/2)
    w3=np.exp(-Dtau*Jz/4)
    # weights of plaquette-graphs
    # vertical
    if g==1:
        w=w1-w2+w3
        # check for allowed vertices
        if n==1 or n==2:
            return w/w1
        elif n==5 or n==6:
            return w/w3
        else:
            return 0
    # horizontal
    elif g==2:
        w=w1+w2-w3
        if n==1 or n==2:
            return w/w1
        elif n==3 or n==4:
            return w/w2
        else:
            return 0
    # combined (neglected)
    elif g==3:
        return 0
    # diagonal
    elif g==4:
        w=-w1+w2+w3
        if n==3 or n==4:
            return w/w2
        elif n==5 or n==6:
            return w/w3
        else:
            return 0