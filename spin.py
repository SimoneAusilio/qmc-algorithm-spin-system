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

def energy (Jx, Jz, config):
    ex=0
    ez=0
    N=len(config)
    for i in range(0, N, 2):
        ex+=S_up(config[i%N])*S_down(config[(i+1)%N])+S_down(config[i%N]*S_up(config[(i+1)%N]))
        ez+=S_z(config[i%N])*S_z(config[(i+1)%N])
    return Jx*ex/2+Jz*ez