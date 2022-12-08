import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections  as mc 
from matplotlib.animation import FuncAnimation
import Projet_Code
import configuration
import functools

L=16
Beta=2
m=8
Jx=3
Jz=1
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
ax1.add_collection(lc)

# energy per spin
ax2=fig.add_subplot(1, 2, 2)
ax2.set_title("Energy per spin")
curve, =ax2.plot([], [], label = "Energy value")
average, =ax2.plot([],[], label = "Average energy")
plt.legend()
ax2.set_xlim(0, N)
ax2.set_ylim(-1, 1)



time = []
energ = []
avrg_e = []
cursor = 0
def worldline_anim(n):
    '''Animation function for update algorithm'''
    # update trial
    for i in range(length_cycle):
        chess.local_update()
    conf._update_configuration(chess)
    e=np.average(np.array([conf._get_energy(i) for i in range(2*conf.m)]))/conf.size

    # plot update (left)
    current_lines=chess._get_worldlines_board()
    current_lc=mc.LineCollection(current_lines, colors=color_red, linewidths=4)
    ax1.collections[0].set_segments(current_lines)
    
    
    # plot update (right)
    if len(time)<N: time.append(n)
    if len(energ)<N: 
        energ.append(e)
        global cursor
        if cursor == 0 : 
            avrg_e.append(e)
            cursor+=1
        else : 
            avrg_e.append((avrg_e[-1]*cursor+e)/(cursor+1))
            cursor += 1
    else:
        energ.insert(N, e)
        avrg_e.append((avrg_e[-1]*cursor+e)/(cursor+1))
        cursor += 1
        energ.pop(0)
        avrg_e.pop(0)
    curve.set_data(time, energ)
    average.set_data(time,avrg_e)

    return (lines, curve, avrg_e)

animation=FuncAnimation(fig, worldline_anim, interval=300, blit=False)
plt.show()