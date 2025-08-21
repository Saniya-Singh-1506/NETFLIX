import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# ---- SETUP 3D FIGURE ----
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection="3d", facecolor="black")
ax.set_xlim(-15,15)
ax.set_ylim(-15,15)
ax.set_zlim(-5,5)
ax.set_xticks([]); ax.set_yticks([]); ax.set_zticks([])

# ---- STARFIELD ----
stars_x = np.random.uniform(-15,15,200)
stars_y = np.random.uniform(-15,15,200)
stars_z = np.random.uniform(-5,5,200)
stars, = ax.plot(stars_x, stars_y, stars_z, "w.", alpha=0.8, markersize=3)

# ---- SUN ----
sun, = ax.plot([0], [0], [0], "o", color="yellow", markersize=50, markeredgecolor="orange")

# ---- PLANETS (cartoon colors) ----
planet_colors = ["deepskyblue", "hotpink", "limegreen", "orange", "violet"]
planet_orbits = [3, 5, 7, 9, 11]   # orbit radius
planet_sizes  = [20, 25, 22, 30, 28]

planets = []
for color, size in zip(planet_colors, planet_sizes):
    p, = ax.plot([0], [0], [0], "o", color=color, markersize=size, markeredgecolor="white")
    planets.append(p)

# ---- ANIMATION FUNCTION ----
def update(frame):
    # Twinkling stars effect
    stars.set_alpha(0.5 + 0.5*np.sin(frame/10.0))

    # Move planets in circular orbits
    for i, (orbit, p) in enumerate(zip(planet_orbits, planets)):
        angle = frame * 0.05 * (i+1)
        x = orbit * np.cos(angle)
        y = orbit * np.sin(angle)
        z = 0.5 * np.sin(frame*0.05 + i)   # slight up/down wobble
        p.set_data([x], [y])
        p.set_3d_properties([z])

    return [stars] + planets

ani = FuncAnimation(fig, update, frames=500, interval=50, blit=True)

plt.show()
