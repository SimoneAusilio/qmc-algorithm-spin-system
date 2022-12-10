import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections  as mc 
from matplotlib.animation import FuncAnimation
import Worldline_chessboard
import configuration
import functools
import graph_chessboard
import vertex
import configurations_initial_worldsquares as cf

L=20
Beta=3
m=9
Jx=3
Jz=1
chess=Worldline_chessboard.Chessboard(L, Beta, m, Jx, Jz,cf.spin_up1(m,L))
chess1 = Worldline_chessboard.Chessboard(L, Beta, m, Jx, Jz,cf.spin_up1(m,L))
chess_graph = graph_chessboard.Graph_chessboard(chess)
conf=configuration.Configuration(chess)
conf2=configuration.Configuration(chess1)

length_cycle=100    # number of update trials (arbitrary for the moment)
N=200   # time steps

# plot worldline configuration and energy (two-panel figure)
fig=plt.figure(figsize=(10, 5))

### LOCAL UPDATE

# worldline configuration
ax3=fig.add_subplot(1, 4, 3)
# ax1.set_title("Worldline configuration")
im=ax3.imshow(chess.binary_chessboard, cmap='binary_r', interpolation='nearest', extent=chess.extent, alpha=1, aspect=1)
color_red=(1, 0, 0, 1)
lines=chess.worldlines_board
lc=mc.LineCollection(lines, colors=color_red, linewidths=4)
ax3.add_collection(lc)
ax3.set_title("Worldlines configuration LOCAL UPDATE")
ax3.set_xlabel("Chaine size L")
ax3.set_ylabel("imaginary axis m")

# energy per spin
ax4=fig.add_subplot(1, 4, 4)
ax4.set_title("Energy per spin")
curve2, =ax4.plot([], [], label = "Energy value LOCAL")
average2, =ax4.plot([],[], label = "Average energy LOCAL")
curve, =ax4.plot([], [], label = "Energy value LOOP")
average, =ax4.plot([],[], label = "Average energy LOOP")
plt.legend()
ax4.set_xlim(0, N)
ax4.set_ylim(-1, 0)



### LOOP UPDATE
# worldline configuration
ax1=fig.add_subplot(1, 4, 1)
# ax1.set_title("Worldline configuration")
im=ax1.imshow(chess.binary_chessboard, cmap='binary_r', interpolation='nearest', extent=chess.extent, alpha=1, aspect=1)
color_red=(1, 0, 0, 1)
lines=chess.worldlines_board
lc=mc.LineCollection(lines, colors=color_red, linewidths=4)
ax1.add_collection(lc)
ax1.set_title("Worldlines configuration")
ax1.set_xlabel("Chaine size L")
ax1.set_ylabel("imaginary axis m")



ax2=fig.add_subplot(1, 4, 2)
ax2.set_title("Worldbreakup configuration")
im=ax2.imshow(chess.binary_chessboard, cmap='binary_r', interpolation='nearest', extent=chess.extent, alpha=1, aspect=1)
color_red=(1, 0, 0, 1)
lines2=chess_graph.lines
lc2=mc.LineCollection(lines2, colors=color_red, linewidths=4)
ax2.add_collection(lc2)
ax2.set_title("Plaquette graph configuration")
ax2.set_xlabel("Chaine size L")
ax2.set_ylabel("imaginary axis m")


# energy per spin
"""
ax3=fig.add_subplot(2, 3, 3)
ax3.set_title("Energy per spin")
curve, =ax3.plot([], [], label = "Energy value")
average, =ax3.plot([],[], label = "Average energy")
plt.legend()
ax3.set_xlim(0, N)
ax3.set_ylim(-1, 0)
"""



time = []
energ = []
energ1 = []
avrg_e = []
avrg_e1 = []
cursor = 0
def worldline_anim(n):
    '''Animation function for update algorithm'''
    # update trial
    for i in range(length_cycle):
        chess_graph._do_loop_update(chess)
        chess1.local_update()
    conf._update_configuration(chess)
    conf2._update_configuration(chess1)
    e=np.average(np.array([conf._get_energy(i) for i in range(2*conf.m)]))/conf.size
    e1 = np.average(np.array([conf2._get_energy(i) for i in range(2*conf2.m)]))/conf2.size

    # plot update (left)
    #loop update
    current_lines=chess._get_worldlines_board()
    current_lc=mc.LineCollection(current_lines, colors=color_red, linewidths=4)
    ax1.collections[0].set_segments(current_lines)

    #local update
    current_lines1=chess1._get_worldlines_board()
    current_lc1=mc.LineCollection(current_lines1, colors=color_red, linewidths=4)
    ax3.collections[0].set_segments(current_lines1)

    current_lines_graph=chess_graph._get_lines_graphboard(chess)
    current_lc_graph=mc.LineCollection(current_lines_graph, colors=color_red, linewidths=4)
    ax2.collections[0].set_segments(current_lines_graph)
    
    
    # plot update (right)
    if len(time)<N: time.append(n)
    if len(energ)<N: 
        energ.append(e)
        energ1.append(e1)
        global cursor
        if cursor == 0 : 
            avrg_e.append(e)
            avrg_e1.append(e1)
            cursor+=1
        else : 
            avrg_e.append((avrg_e[-1]*cursor+e)/(cursor+1))
            avrg_e1.append((avrg_e1[-1]*cursor+e1)/(cursor+1))
            cursor += 1
    else:
        energ.insert(N, e)
        energ1.insert(N, e1)
        avrg_e.append((avrg_e[-1]*cursor+e)/(cursor+1))
        avrg_e1.append((avrg_e1[-1]*cursor+e1)/(cursor+1))

        cursor += 1
        energ.pop(0)
        avrg_e.pop(0)
        energ1.pop(0)
        avrg_e1.pop(0)
    curve.set_data(time, energ)
    average.set_data(time,avrg_e)
    curve2.set_data(time, energ1)
    average2.set_data(time,avrg_e1)

    return (lines, curve, average, curve2, average2)

animation=FuncAnimation(fig, worldline_anim, interval=1, blit=False)
plt.show()


'''
# data collection
n_warmup=100    # number of simulations made at the beginning
n_cycles=100    # number of measurements

beta_range=np.arange()'''