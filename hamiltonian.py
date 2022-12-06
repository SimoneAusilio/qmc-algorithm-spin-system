import numpy as np
from numpy.linalg import eigh
import spin
from configuration import Configuration

def hamiltonian(ket, Jx, Jz):
    '''Applies the hamiltonian operator to a spin configuration'''
    # ket: Nx2 matrix (N number of spins)
    N=len(ket)
    new_state=np.zeros((N, 2))
    if N==2:
        for j in range(N-1):
            new_state[j]=Jx/2*(np.dot(spin.S_up_vec(ket[j]), spin.S_down_vec(ket[(j+1)%N]))+\
                    np.dot(spin.S_up_vec(ket[(j+1)%N]), spin.S_down_vec(ket[j])))+\
                    Jz*np.dot(spin.S_z_vec(ket[j]), spin.S_z_vec(ket[(j+1)%N]))
    else:
        for j in range(N):
            new_state[j]=Jx/2*(np.dot(spin.S_up_vec(ket[j]), spin.S_down_vec(ket[(j+1)%N]))+\
                    np.dot(spin.S_up_vec(ket[(j+1)%N]), spin.S_down_vec(ket[j])))+\
                    Jz*np.dot(spin.S_z_vec(ket[j]), spin.S_z_vec(ket[(j+1)%N]))
    return new_state

def braket(bra, ket):
    '''Returns the braket product between two configurations'''
    p=0.
    for j in range(len(bra)):
        p+=np.dot(bra[j], ket[j])
    return p

def to_spin(config):
    '''Converts from spin sign configuration to vector configuration'''
    N=len(config)
    c=np.zeros((N, 2))
    for i in range(N):
        c[i][0]=1 if config[i]==+1 else 0
        c[i][1]=1 if config[i]==-1 else 0
    return c

def hamiltonian_matrix(base, Jx, Jz):
    '''Calculates the hamiltonian matrix in the input base'''
    N=len(base)
    H=np.zeros((N, N))
    for i in range(N):
        for j in range(i, N):
            H[i][j]=braket(to_spin(base[i]), hamiltonian(to_spin(base[j]), Jx, Jz))
            if j!=i: H[j][i]=H[i][j]
    return H

# test for 2, 3, 4 spins
base_2=np.vstack(([1, 1], [-1, 1], [1, -1], [-1, -1]))
print(braket(to_spin(base_2[0]), to_spin(base_2[0])))
# print(hamiltonian_matrix(base_2, Jx=1, Jz=2))
# energies_2=eigh(hamiltonian_matrix(base_2, Jx=1, Jz=2))[0]
# print(energies_2)

'''base_3=np.vstack(([1, 1, 1], [-1, 1, 1], [1, -1, 1], [1, 1, -1], [-1, -1, 1], [-1, 1, -1], [1, -1, -1], [-1, -1, -1]))
energies_3=eigh(hamiltonian_matrix(base_3, Jx=1, Jz=2))[0]'''

'''base_4=np.vstack(([1, 1, 1, 1], [-1, 1, 1, 1], [1, -1, 1, 1], [1, 1, -1, 1], [1, 1, 1, -1],\
        [-1, -1, 1, 1], [-1, 1, -1, 1], [-1, 1, 1, -1], [1, -1, -1, 1], [1, -1, 1, -1],\
            [1, 1, -1, -1], [-1, -1, -1, 1], [-1, -1, 1, -1], [1, -1, -1, -1], [-1, 1, -1, -1],
            [-1, -1, -1, -1]))'''