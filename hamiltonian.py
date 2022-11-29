import numpy as np
from numpy.linalg import eigh
import spin
from configuration import Configuration

def hamiltonian(ket, Jx, Jz):
    '''Applies the hamiltonian operator to a spin configuration'''
    N=len(ket)
    new_state=np.zeros(N)
    for j in range(N):
        new_state[j]=Jx/2*(spin.S_up(ket[j])*spin.S_down(ket[(j+1)%N])+\
                spin.S_up(ket[(j+1)%N])*spin.S_down(ket[j]))+\
                Jz*(spin.S_z(ket[(j+1)%N])*spin.S_z(ket[j]))
    return new_state

# TODO
def braket(bra, ket):
    '''Returns the braket product between two configurations'''
    p=0.
    for j in range(len(bra)):
        p+=bra[j]*ket[j]
    return p

def hamiltonian_matrix(base, Jx, Jz):
    '''Calculates the hamiltonian matrix in the input base'''
    N=len(base)
    H=np.zeros((N, N))
    for i in range(N):
        for j in range(i, N):
            H[i][j]=braket(base[i], hamiltonian(base[j], Jx, Jz))
            if j!=i: H[j][i]=H[i][j]
    return H

# test for N=2
#base_2=np.vstack(([1, 1], [-1, 1], [1, -1], [-1, -1]))

# base_3=np.vstack([1, 1, 1], [-1, 1, 1], [1, -1, 1], [1, 1, -1], [-1, -1, 1], [-1, 1, -1], [1, -1, -1], [-1, -1, -1])

'''base_4=np.vstack([1, 1, 1, 1], [-1, 1, 1, 1], [1, -1, 1, 1], [1, 1, -1, 1], [1, 1, 1, -1],\
        [-1, -1, 1, 1], [-1, 1, -1, 1], [-1, 1, 1, -1], [1, -1, -1, 1], [1, -1, 1, -1],\
            [1, 1, -1, -1], [-1, -1, -1, 1], [-1, -1, 1, -1], [1, -1, -1, -1], [-1, 1, -1, -1],
            [-1, -1, -1, -1]\)'''