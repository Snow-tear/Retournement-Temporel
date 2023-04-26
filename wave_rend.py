import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from paramètres import *

u=np.load('u.npy')

fig, ax = plt.subplots(figsize=(16, 9))
u_min, u_max = np.min(u), np.max(u)

def animate(i):
    ax.clear()
    ax.set_xlim([0, Lx])
    ax.set_ylim([0, Ly])
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("2D Wave Animation")
    ax.imshow(u[i].T, cmap="jet", vmin=u_min, vmax=u_max, extent=[0, Lx, 0, Ly])
    return ax


anim = animation.FuncAnimation(fig, animate, frames=Nt, interval=50)
anim.save("./wave/"+para_string+".mp4", writer="ffmpeg", fps=30)