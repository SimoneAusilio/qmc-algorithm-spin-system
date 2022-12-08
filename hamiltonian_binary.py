import numpy as np
from numpy.linalg import eigh

'''Basis of N spin configurations (dimension 2**N) written as binary number (1: up, 0: down)
Corresponding index can be taken with int()
Conversion of binary number to binary string needed to manipulate configuration'''

def to_binary_str(bin_num, L):
    '''Converts from binary number to binary string (returned as a list)'''
    # taken from https://stackoverflow.com/a/13081133
    if bin_num==None:
        return None
    # check if length of binary number corresponds to L
    l=len(bin(bin_num)[2:]) # take out initial 0b
    string=''
    if l!=L:
        string+='0'*(L-l)
    string+=str(bin(bin_num))[2:]
    return [bit for bit in string]

def to_binary_num(bin_str):
    '''Converts from binary string to binary spin configuration'''
    # invalid string
    # taken from https://stackoverflow.com/a/28836394
    if None in bin_str:
        return None
    # format list to string
    # taken from https://stackoverflow.com/a/47851872
    string=''
    for el in bin_str:
        string+=el
    return int(string, 2)

def S_up(bin_num, i, L):
    '''Returns the binary number associated with the raising of the i-th spin'''
    if bin_num==None:
        return None
    list=to_binary_str(bin_num, L)
    # None is returned when a spin up is raised
    list[i]='1' if list[i]=='0' else None
    return to_binary_num(list)

def S_down(bin_num, i, L):
    '''Returns the binary number associated with the lowering of the i-th spin'''
    if bin_num==None:
        return None
    list=to_binary_str(bin_num, L)
    # None is returned when a spin down is lowered
    list[i]='0' if list[i]=='1' else None
    return to_binary_num(list)

def S_z(bin_num, L):
    '''Returns the eigenvalue associated to the application of the S_z operators
    to the configuration'''
    if bin_num==None:
        return None
    bin_str=to_binary_str(bin_num, L)
    N=len(bin_str)
    val=0.
    # N=2: only one link
    if N==2:
        val=0.25 if bin_str[0]==bin_str[1] else -0.25
    # N!=2: N links
    else:
        for i in range(N):
            # (-)0.5*0.5 if spin are (anti)parallel
            val+=0.25 if bin_str[i]==bin_str[(i+1)%N] else -0.25
    return val

def hamiltonian(bin_num, L):
    '''Returns a list of spin configurations deriving from the application
    of the raising and lowering operators of the hamiltonian to the original one'''
    N=len(to_binary_str(bin_num, L))
    list=[]
    for i in range(N):
        a=S_down(bin_num, (i+1)%N, L)
        b=S_up(bin_num, (i+1)%N, L)
        list.append(S_up(a, i, L))
        list.append(S_down(b, i, L))
    return list

def hamiltonian_matrix(L, Jx, Jz):
    '''Calculates the hamiltonian matrix in the input base'''
    P=2**L
    H=np.zeros((P, P))
    for i in range(P):
        H[i][i]+=Jz*S_z(i, L)
        for j in range(i, P):
            H[i][j]+=0.5*Jx if i in hamiltonian(j, L) else 0
            if j!=i:
                H[j][i]=H[i][j]
    return H

energies=eigh(hamiltonian_matrix(2, Jx=1, Jz=2))[0]
print(energies)