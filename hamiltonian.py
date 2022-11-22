import numpy as np
import spin

def hamiltonian(old_state):
    N=old_state.length
    new_state=np.zeros(N)