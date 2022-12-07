import numpy as np
from square import Square

def prob(n: int, breakup_type: int, Dtau: float, Jx: float, Jz: float):
    '''Returns the probability of an allowed breakup on a vertex (<->square type)'''
    
    # weights of vertices
    w1=np.exp(Dtau*Jx/4)*np.cosh(Dtau*Jx/2)
    w2=np.exp(-Dtau*Jx/4)*np.sinh(Dtau*Jx/2)
    w3=np.exp(-Dtau*Jz/4)
    print("W1:",w1)
    print("W2:",w2)
    print("w3:",w3)
    # weights of plaquette-graphs
    # vertical
    if breakup_type==1:
        w=(w1-w2+w3)/2
        # check for allowed vertices
        if n==1 or n==2:
            return w/w1
        elif n==5 or n==6:
            return w/w3
        else:
            return 0
    # horizontal
    elif breakup_type==2:
        w=(w1+w2-w3)/2
        if n==1 or n==2:
            return w/w1
        elif n==3 or n==4:
            return w/w2
        else:
            return 0
    # combined (neglected)
    elif breakup_type==3:
        return 0
    # diagonal
    elif breakup_type==4:
        w=(-w1+w2+w3)/2
        if n==3 or n==4:
            return w/w2
        elif n==5 or n==6:
            return w/w3
        else:
            return 0