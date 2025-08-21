import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Figure setup
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor("black")
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')  # Hide axes for a cleaner look

# Create the "couple" points
man, = ax.plot([], [], 'o', color="cyan", markersize=14)
woman, = ax.plot([], [], 'o', color="magenta", markersize=14)
line, = ax.plot([], [], color="white", lw=1, alpha=0.5)  # line connecting them

# Parametric motion variables
t_vals = np.linspace(0, 2*np.pi, 200)

def init():
    man.set_data([], [])
    woman.set_data([], [])
    line.set_data([], [])
    return man, woman, line

def update(frame):
    # Make them orbit each other like dancing
    t = frame / 10
    x1 = np.cos(t)  # Man's X
    y1 = np.sin(t)  # Man's Y
    x2 = np.cos(t + np.pi/3) * 0.8  # Woman's X
    y2 = np.sin(t + np.pi/3) * 0.8  # Woman's Y

    man.set_data(x1, y1)
    woman.set_data(x2, y2)
    line.set_data([x1, x2], [y1, y2])
    return man, woman, line

# Create animation
ani = animation.FuncAnimation(fig, update, frames=300, init_func=init,
                              interval=30, blit=True)

plt.show()
