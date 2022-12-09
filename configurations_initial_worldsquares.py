import numpy as np 
from square import Square

def spin_up1(m,L):
    "initializing the white square of the chessboard with fixed wordline configuration"
    tab = np.empty((2*m,L), dtype=Square)
    for j in range(L):
        for i in range(2*m):
            if (i+j)%2 == 0:
                "if there are black square, no information is needed"
                tab[i][j] = np.nan
            elif j==1 and i%2==0:
                tab[i][j] = Square(1)
            elif j == 0 and i%2==1:
                tab[i][j] = Square(2)
            else : 
                tab[i][j] = Square(6)
    return tab

def spin_up2(m,L):
    "initializing the white square of the chessboard with fixed wordline configuration"
    tab = np.empty((2*m,L), dtype=Square)
    for j in range(L):
        for i in range(2*m):
            if (i+j)%2 == 0:
                "if there are black square, no information is needed"
                tab[i][j] = np.nan
            elif j==1 and i%2==0:
                tab[i][j] = Square(5)
            elif  j==0 and i%2==1:
                tab[i][j] = Square(2)
            elif  j==2 and i%2==1:
                tab[i][j] = Square(1)
            else : 
                tab[i][j] = Square(6)
    return tab

def spin_up3(m,L):
    "initializing the white square of the chessboard with fixed wordline configuration"
    tab = np.empty((2*m,L), dtype=Square)
    for j in range(L):
        for i in range(2*m):
            if (i+j)%2 == 0:
                "if there are black square, no information is needed"
                tab[i][j] = np.nan
            elif j==1 and i%2==0:
                tab[i][j] = Square(5)
            elif j==2 and i%2==1:
                tab[i][j] = Square(5)
            elif j == 0 and i%2==1:
                tab[i][j] = Square(2)
            elif j== 3 and i%2 == 0:
                tab[i][j] = Square(1)
            else : 
                tab[i][j] = Square(6)
    return tab

def spin_up_all(m,L):
    "initializing the white square of the chessboard with fixed wordline configuration"
    tab = np.empty((2*m,L), dtype=Square)
    for j in range(L):
        for i in range(2*m):
            if (i+j)%2 == 0:
                "if there are black square, no information is needed"
                tab[i][j] = np.nan
            else:
                tab[i][j]= Square(5)
    return tab

def spin_up_none(m,L):
    "initializing the white square of the chessboard with fixed wordline configuration"
    tab = np.empty((2*m,L), dtype=Square)
    for j in range(L):
        for i in range(2*m):
            if (i+j)%2 == 0:
                "if there are black square, no information is needed"
                tab[i][j] = np.nan
            else:
                tab[i][j]= Square(6)
    return tab

def classic_1_over_2(m,L):
    "initializing the white square of the chessboard with fixed wordline configuration"
    tab = np.empty((2*m,L), dtype=Square)

    for j in range(L):
        for i in range(2*m):
            if (i+j)%2 == 0:
                "if there are black square, no information is needed"
                tab[i][j] = np.nan
            else:
                "instantiating white squares"
                if j%2 == 0:
                    tab[i][j] =Square(2)
                else : tab[i][j] =Square(1)
    return tab

def classic_1_over_4(m,L):
    "initializing the white square of the chessboard with fixed wordline configuration"
    tab = np.empty((2*m,L), dtype=Square)

    for j in range(L):
        for i in range(2*m):
            if (i+j)%2 == 0:
                "if there are black square, no information is needed"
                tab[i][j] = np.nan
            else:
                "instantiating white squares"
                if j%4 == 0 and i%2 == 1:
                    self.worldsquare_board[i][j] = Square(2)
                elif j%4 == 1 and i%2 == 0:
                    self.worldsquare_board[i][j] = Square(1)
                else: 
                    self.worldsquare_board[i][j] = Square(6)
                
    return tab
