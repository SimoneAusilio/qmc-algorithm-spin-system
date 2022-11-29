import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections  as mc 
from matplotlib.animation import FuncAnimation
import Projet_Code
import configuration
import functools

L=6
Beta=20
m=3
Jx=1
Jz=2
chess=Projet_Code.Chessboard(L, Beta, m, Jx, Jz)
conf=configuration.Configuration(chess)

length_cycle=100    # number of update trials (arbitrary for the moment)
N=200   # time steps

# plot worldline configuration and energy (two-panel figure)
fig=plt.figure(figsize=(10, 5))
# worldline configuration
ax1=fig.add_subplot(1, 2, 1)
# ax1.set_title("Worldline configuration")
im=ax1.imshow(chess.binary_chessboard, cmap='binary_r', interpolation='nearest', extent=chess.extent, alpha=1, aspect=1)
color_red=(1, 0, 0, 1)
lines=chess.worldlines_board
lc=mc.LineCollection(lines, colors=color_red, linewidths=4)
#ax1.add_collection(lc)
# energy per spin
ax2=fig.add_subplot(1, 2, 2)
ax2.set_title("Energy per spin")
curve, =ax2.plot([], [])
ax2.set_xlim(0, N)
ax2.set_ylim(-1, 1)



time=[]
energ=[]

def worldline_anim(n):
    '''Animation function for update algorithm'''
    # keeping track of the old lines
    old_lines = chess._get_worldlines_board()
    old_lc=mc.LineCollection(old_lines, colors=color_red, linewidths=4)
    old_lc.remove()
    # update trial
    for i in range(length_cycle):
        chess.local_update()
    e=np.average(np.array([conf._get_energy(i) for i in range(2*conf.m)]))/conf.size
    # plot update (left)
    current_lines=chess._get_worldlines_board()
    current_lc=mc.LineCollection(current_lines, colors=color_red, linewidths=4)
    ax1.add_collection(current_lc)
    
    #current_lc.remove()
    # plot update (right)
    if len(time)<N: time.append(n)
    if len(energ)<N: energ.append(e)
    else:
        energ.insert(N, e)
        energ.pop(0)
    curve.set_data(time, energ)
    return (lines, curve)

animation=FuncAnimation(fig, worldline_anim, interval=1, blit=False)
plt.show()
'''
# data collection
n_warmup=100    # number of simulations made at the beginning
n_cycles=100    # number of measurements

beta_range=np.arange()'''