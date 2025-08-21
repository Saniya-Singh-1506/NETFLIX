import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create figure
fig, ax = plt.subplots()
ax.set_facecolor("black")
ax.axis("off")

# Data for spiral
theta = np.linspace(0, 20*np.pi, 1000)
r = np.linspace(0, 1, 1000)

x = r * np.cos(theta)
y = r * np.sin(theta)
colors = plt.cm.hsv(np.linspace(0, 1, len(x)))

# Line
line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def update(frame):
    line.set_data(x[:frame], y[:frame])
    line.set_color(colors[frame])
    return line,

ani = animation.FuncAnimation(fig, update, frames=len(x), init_func=init,
                              interval=5, blit=True)

plt.show()
