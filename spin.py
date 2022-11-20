import configuration

'''Spin operators'''
def S_z (sign):
    '''Returns the eigenvalue of spin up or down'''
    return sign*1/2

def S_up (sign):
    '''Climbs the spin down'''
    return -sign if sign==-1 else 0

def S_down (sign):
    '''Descends the spin up'''
    return -sign if sign==1 else 0

def energy (conf, i):
    '''Returns the energy of the configuration at the i-th row'''
    ex=0
    ez=0
    N=conf.size
    chain=conf.config[i]
    for j in range(0, N, 2):
        ex+=S_up(chain[j%N])*S_down(chain[(j+1)%N])+S_down(chain[j%N]*S_up(chain[(j+1)%N]))
        ez+=S_z(chain[j%N])*S_z(chain[(j+1)%N])
    return conf.Jx*ex/2+conf.Jz*ez