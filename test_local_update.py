import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import Projet_Code
import configuration

L=5
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
im=ax1.imshow(chess._config_to_image(), interpolation="none")
# energy per spin
ax2=fig.add_subplot(1, 2, 2)
ax2.set_title("Energy per spin")
line, =ax2.plot([], [])
ax2.set_xlim(0, N)
ax2.set_ylim(-1, 1)

time=[]
energ=[]

def worldline_anim(n, chess, update=Projet_Code.local_update):
        '''Animation function for update algorithm'''
        # update trial
        for i in range(length_cycle):
            chess.update()
        e=np.average(np.array([conf.get_energy(i) for i in range(2*conf.m)]))/conf.size
        # plot update
        im.set_array(chess._config_to_image())
        if len(time)<N: time.append(n)
        if len(energ)<N: energ.append(e)
        else:
            energ.insert(N, e)
            energ.pop(0)
        line.set_data(time, energ)
        return (im, line)

animation=FuncAnimation(fig, worldline_anim, interval=1, blit=False)
plt.show()

# data collection
n_warmup=100    # number of simulations made at the beginning
n_cycles=100    # number of measurements

beta_range=np.arange()