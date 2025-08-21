import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create figure
fig, ax = plt.subplots()
ax.set_facecolor("black")
ax.set_xlim(0, 4*np.pi)
ax.set_ylim(-1.5, 1.5)
ax.set_title("Professional Sine Wave Animation", color="white", fontsize=14)
ax.tick_params(colors='white')

# Generate x data
x = np.linspace(0, 4*np.pi, 500)
line, = ax.plot([], [], lw=2, color="cyan")

def init():
    line.set_data([], [])
    return line,

def update(frame):
    y = np.sin(x - 0.05 * frame)  # Wave motion
    line.set_data(x, y)
    return line,

ani = animation.FuncAnimation(fig, update, frames=200, init_func=init,
                              interval=20, blit=True)

plt.show()
