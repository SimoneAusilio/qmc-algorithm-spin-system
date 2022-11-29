import numpy as np
import numpy.random as rnd
import configuration
from square import Square
import Projet_Code

def to_vertices(sq):
    '''Returns a 2x2 matrix with the direction of the arrows
    +1(-1): arrow pointing inwards (outwards)'''
    n=Square._get_square_type(sq)
    arrows=np.zeros((2, 2), dtype=int)
    if n==1:
        arrows[0][0]=-1
        arrows[0][1]=+1
        arrows[1][1]=-1
        arrows[1][0]=+1
    elif n==2:
        arrows[0][0]=+1
        arrows[0][1]=-1
        arrows[1][1]=+1
        arrows[1][0]=-1
    elif n==3:
        arrows[0][0]=-1
        arrows[0][1]=+1
        arrows[1][1]=+1
        arrows[1][0]=-1
    elif n==4:
        arrows[0][0]=+1
        arrows[0][1]=-1
        arrows[1][1]=-1
        arrows[1][0]=+1
    elif n==5:
        arrows[0][0]=-1
        arrows[0][1]=-1
        arrows[1][1]=+1
        arrows[1][0]=+1
    elif n==6:
        arrows[0][0]=+1
        arrows[0][1]=+1
        arrows[1][1]=-1
        arrows[1][0]=-1
    return arrows

# TODO: write translation from vertices to square to_square(v)
def to_square(v):
    '''Returns the type '''
    if v==np.array([[-1, +1], [-1, +1]]):
        return 1
    elif v==np.array([[+1, 1], [+1, -1]]):
        return 2
    elif v==np.array([[-1, +1], [+1, -1]]):
        return 3
    elif v==np.array([[+1, -1], [-1, +1]]):
        return 4
    elif v==np.array([[-1, -1], [+1, +1]]):
        return 5
    elif v==np.array([[+1, +1], [-1, -1]]):
        return 6
    # there is not the same number of inward and outward arrows
    else:
        return 0

def loop(chess: Projet_Code.Chessboard, random=True):
    '''Makes a random loop and then flips the arrows of the path'''
    # starting square and arrow (chosen at random)
    # TODO: make sure that the square picked is white!
    i, j=rnd.randint(0, 2*chess.m), rnd.randint(0, chess.size)
    mu, nu=rnd.randint(0, 2), rnd.randint(0, 2)
    # loop creation
    path=np.array([i, j, mu, nu])
    a, b=i, j
    rho, sigma=mu, nu
    # emulation of do-while loop to create the path
    while True:
        v=to_vertices(chess.worldsquare_board[i][j])
        # outward arrow
        if v[rho][sigma]==-1:
            # upper square
            if rho==0:
                a=a-1 if a!=0 else 2*chess.m-1
                # left
                if sigma==0:
                    b=b-1 if b!=0 else chess.size-1
                    rho, sigma=1, 1
                #right
                else:
                    b=(b+1)%chess.size
                    rho, sigma=1, 0
            # lower square
            else:
                a=(a+1)%2*chess.m
                if sigma==0:
                    b=b-1 if b!=0 else chess.size-1
                    rho, sigma=0, 1
                else:
                    b=(b+1)%chess.size
                    rho, sigma=0, 0
        # inward arrow
        # TODO: correct snippet   
        else:
            # find the outward arrows
            pos=np.where(v==-1)
            # choose randomly the next direction
            rho, sigma=rnd.choice(pos)
        path=np.vstack(path, [a, b, rho, sigma])
        # returned to starting point?
        if (path[-1].equal([i, j, mu, nu])):
            path.pop()
            break
    # flip the arrows and change the squares
    # TODO: add the case of inward arrow (where square type still don't change)
    for k in range(len(path)):
        v=to_vertices(chess.worldsquare_board[path[0]][path[1]])
        v[path[2]][path[3]]*=-1
        n=to_square(v)
        if n!=0:
            chess.worldsquare_board[path[0]][path[1]]._update(n)