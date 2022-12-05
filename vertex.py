import numpy as np
import numpy.random as rnd
import configuration
from square import Square
import Projet_Code

def to_vertices(sq: Square):
    '''Returns a 2x2 matrix with the direction of the arrows
    +1(-1): arrow pointing inwards (outwards)'''
    n=sq._get_square_type()
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
    elif n==4:
        arrows[0][0]=-1
        arrows[0][1]=+1
        arrows[1][1]=+1
        arrows[1][0]=-1
    elif n==3:
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

def to_square(v: np.array):
    '''Returns the square type'''
    if np.array_equal(v, np.array([[-1, +1], [+1, -1]])):
        return 1
    elif np.array_equal(v, np.array([[+1, -1], [-1, +1]])):
        return 2
    elif np.array_equal(v, np.array([[-1, +1], [-1, +1]])):
        return 4
    elif np.array_equal(v, np.array([[+1, -1], [+1, -1]])):
        return 3
    elif np.array_equal(v, np.array([[-1, -1], [+1, +1]])):
        return 5
    elif np.array_equal(v, np.array([[+1, +1], [-1, -1]])):
        return 6
    # there is not the same number of inward and outward arrows
    else:
        return 0


def is_in(list,a):
    for i in range (len(list)):
        if list[i]==a:
            return (True,i)
    return (False,None)

def loop(chess: Projet_Code.Chessboard, random=True):
    key = 0
    '''Makes a random loop and then flips the arrows of the path'''
    # starting square and arrow (chosen at random)
    # make sure that the picked square is white!
    i, j=0, 0
    while (i+j)%2!=1:
        i, j=rnd.randint(0, 2*chess.m), rnd.randint(0, chess.size)
    
    #print("begin in ",i,j)
    mu, nu=rnd.randint(0, 2), rnd.randint(0, 2)
    # loop creation
    path=np.array([i, j, mu, nu])
    
    #k=0
    #print("Step "+str(k))
    #k+=1
    #print("path :", path)
    
    a, b=i, j
    visited_cube = [(i,j)]
    rho, sigma=mu, nu

    # emulation of do-while loop to create the path
    while True:
        track_outward = True #to verify in which case we are, summing up all square visited and knowing when there is the loop
        key +=1 #a verification that the algorithm will not loop infinitly,if key>500 return False
        
        #print(a,b,"what square", chess.worldsquare_board[a][b]._get_square_type())
        v=to_vertices(chess.worldsquare_board[a][b])
        #print("vertice de ", a, b ,": ",v)
        
        # outward arrow
        if v[rho][sigma] == -1:
            #print("outward arrow")
            
            # upper square
            if rho == 0:
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
                a=(a+1)%(2*chess.m)
                if sigma == 0:
                    b=b-1 if b!=0 else chess.size-1
                    rho, sigma=0, 1
                else:
                    b=(b+1)%chess.size
                    rho, sigma=0, 0
            

        # inward arrow 
        else:
            #print("inward arrow")
            
            track_outward = False
            # find the outward arrows
        
            pos = []
            for k1 in range(2):
                for k2 in range(2):
                    if v[k1][k2] == -1:
                        pos.append([k1,k2])
            #print("pos1,pos2 :",pos)
            
            # choose randomly the next direction
            d=rnd.choice((1, 2))
            rho, sigma=pos[0] if d==1 else pos[1]

        path=np.vstack((path, [a, b, rho, sigma]))
        #print("Step "+str(k))
        #k+=1
        #print("new path: ",path)

        # returned to starting point?
        
        #print(track_outward)
        #print("a,b",a,b)
        #print("i,j",i,j)
        boolean,indice = is_in(visited_cube,(a,b))
        #print("indice :",indice)
        if boolean and track_outward:
            #print("we should break")
            #print("path before cut",path)
            path = path[indice:]
            #print("path after cut",path)
            break
        else : 
            visited_cube.append((a,b))
        if key == 500: 
            print("échec")
            return False
    # flip the arrows and change the squares
    #if the first arrow is inward we delete it
    #the first arrow is then always outward and we can flip two by two
    
    v=to_vertices(chess.worldsquare_board[path[0][0]][path[0][1]])
    
    #print("first vertice",v)
    if v[path[0][2]][path[0][3]]== 1:
        #print("change")
        path = path[1:]
    
    #putting the inward and outward arrow near each other
    path = np.vstack((path,path[0]))
    path = path[1:]
    #print("ensemble path :", path)
    for k in range(0,len(path),2):
        v=to_vertices(chess.worldsquare_board[path[k][0]][path[k][1]])
        #print("ex vertice",v)
        v[path[k][2]][path[k][3]]*=-1
        v[path[k+1][2]][path[k+1][3]]*=-1
        #print("new vertice:",v)
        n=to_square(v)
        #print("new n :",n)
        if n!=0:
            #print(n)
            chess.worldsquare_board[path[k][0]][path[k][1]]._update(n)
        chess.worldlines_board = chess._get_worldlines_board()
    print("loop done")

