import numpy as np

'''Spin operators'''

def S_z(sign: int):
    '''Returns the eigenvalue of spin up or down'''
    return sign*1/2

def S_z_vec(spin: np.array):
    '''Applies S_z to a spinor'''
    return np.array([0.5*spin[0], -0.5*spin[1]])

def S_up(sign: int):
    '''Raises the spin down'''
    return -sign if sign==-1 else 0

def S_up_vec(spin: np.array):
    '''Raises the spinor down'''
    return np.array([spin[1], 0])

def S_down(sign: int):
    '''Lowers the spin up'''
    return -sign if sign==1 else 0

def S_down_vec(spin: np.array):
    '''Lowers the spinor up'''
    return np.array([0, spin[0]])

def energy(conf, i: int):
    '''Returns the energy of the configuration at the i-th row'''
    ex=0
    ez=0
    N=conf.size
    chain=conf.config[i]
    for j in range(0, N, 2):
        ex+=S_up(chain[j%N])*S_down(chain[(j+1)%N])+S_down(chain[j%N]*S_up(chain[(j+1)%N]))
        ez+=S_z(chain[j%N])*S_z(chain[(j+1)%N])
    return conf.Jx*ex/2+conf.Jz*ez