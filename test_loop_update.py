import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections  as mc 
from matplotlib.animation import FuncAnimation
import Projet_Code
import configuration
import functools
import graph_chessboard
import vertex

L=4
Beta=4
m=12
Jx=3
Jz=1
chess=Projet_Code.Chessboard(L, Beta, m, Jx, Jz)
chess_graph = graph_chessboard.Graph_chessboard(chess)
conf=configuration.Configuration(chess)

length_cycle=100    # number of update trials (arbitrary for the moment)
N=200   # time steps

# plot worldline configuration and energy (two-panel figure)
fig=plt.figure(figsize=(10, 5))
# worldline configuration
ax1=fig.add_subplot(1, 3, 1)
# ax1.set_title("Worldline configuration")
im=ax1.imshow(chess.binary_chessboard, cmap='binary_r', interpolation='nearest', extent=chess.extent, alpha=1, aspect=1)
color_red=(1, 0, 0, 1)
lines=chess.worldlines_board
lc=mc.LineCollection(lines, colors=color_red, linewidths=4)
ax1.add_collection(lc)
ax1.set_title("Worldlines configuration")
ax1.set_xlabel("Chaine size L")
ax1.set_ylabel("imaginary axes m")



ax2=fig.add_subplot(1, 3, 2)
ax2.set_title("Worldbreakup configuration")
im=ax2.imshow(chess.binary_chessboard, cmap='binary_r', interpolation='nearest', extent=chess.extent, alpha=1, aspect=1)
color_red=(1, 0, 0, 1)
lines2=chess_graph.lines
lc2=mc.LineCollection(lines2, colors=color_red, linewidths=4)
ax2.add_collection(lc2)
ax2.set_title("Plaquette graph configuration")
ax2.set_xlabel("Chaine size L")
ax2.set_ylabel("imaginary axes m")


# energy per spin
ax3=fig.add_subplot(1, 3, 3)
ax3.set_title("Energy per spin")
curve, =ax3.plot([], [], label = "Energy value")
average, =ax3.plot([],[], label = "Average energy")
plt.legend()
ax3.set_xlim(0, N)
ax3.set_ylim(-1, 0)



time = []
energ = []
avrg_e = []
cursor = 0
def worldline_anim(n):
    '''Animation function for update algorithm'''
    # update trial
    for i in range(length_cycle):
        chess_graph._do_loop_update(chess)
    conf._update_configuration(chess)
    e=np.average(np.array([conf._get_energy(i) for i in range(2*conf.m)]))/conf.size

    # plot update (left)
    current_lines=chess._get_worldlines_board()
    current_lc=mc.LineCollection(current_lines, colors=color_red, linewidths=4)
    ax1.collections[0].set_segments(current_lines)

    current_lines_graph=chess_graph._get_lines_graphboard(chess)
    current_lc_graph=mc.LineCollection(current_lines_graph, colors=color_red, linewidths=4)
    ax2.collections[0].set_segments(current_lines_graph)
    
    
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

    return (lines, curve, average)

animation=FuncAnimation(fig, worldline_anim, interval=1, blit=False)
plt.show()


'''
# data collection
n_warmup=100    # number of simulations made at the beginning
n_cycles=100    # number of measurements

beta_range=np.arange()'''