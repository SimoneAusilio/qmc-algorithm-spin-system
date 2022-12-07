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
    s=str(bin(bin_num))[2:]
    return [bit for bit in s]

# TODO
def to_binary_num(bin_str):
    '''Converts from binary string to binary spin configuration'''
    # invalid string
    # taken from https://stackoverflow.com/a/28836394
    if None in bin_str:
        return None
    # format list to string
    # taken from https://stackoverflow.com/a/47851872
    s=''
    for el in bin_str:
        s+=el
    num=int(s, 2)
    return num

print(to_binary_num(["1", "0", "1"]))

def S_up(bin_num, i):
    '''Returns the binary number associated with the raising of the i-th spin'''
    if bin_num==None:
        return None
    list=to_binary_str(bin_num)
    # None is returned when a spin up is raised
    list[i]='1' if list[i]=='0' else None
    return to_binary_num(list)

def S_down(bin_num, i):
    '''Returns the binary number associated with the lowering of the i-th spin'''
    if bin_num==None:
        return None
    list=to_binary_str(bin_num)
    # None is returned when a spin down is lowered
    list[i]='0' if list[i]=='1' else None
    return to_binary_num(list)

def S_z(bin_num):
    '''Returns the eigenvalue associated to the application of the S_z operators
    to the configuration'''
    if bin_num==None:
        return None
    bin_str=to_binary_str(bin_num)
    N=len(bin_str)
    val=0.
    for i in range(N):
        val+=0.25 if bin_str[i]==bin_str[(i+1)%N] else -0.25
    return val

def hamiltonian(bin_num):
    '''Returns a list of spin configurations deriving from the application
    of the raising and lowering operators of the hamiltonian to the original one'''
    N=len(to_binary_str(bin_num))
    list=[]
    for i in range(N):
        a=S_down(bin_num, (i+1)%N)
        b=S_up(bin_num, (i+1)%N)
        list.append(S_up(a, i))
        list.append(S_down(b, i))
    return list

# print(hamiltonian(0b110))

def hamiltonian_matrix(base, Jx, Jz):
    '''Calculates the hamiltonian matrix in the input base'''
    L=len(base)
    H=np.zeros((L, L))
    for i in range(L):
        for j in range(i, L):
            for k in hamiltonian(bin(j)):
                H[i][j]+=0.5*Jx if bin(i)==k else 0
            if j==i:
                H[i][j]+=Jz*S_z(bin(i))
            if j!=i:
                H[j][i]=H[i][j]
    return H

def construct_basis(N):
    '''Constructs a basis of possible configurations with binary numbers'''
    return [bin(i) for i in range(2**N)]

# energies=eigh(hamiltonian_matrix(construct_basis(2), Jx=1, Jz=2))
# print(energies)