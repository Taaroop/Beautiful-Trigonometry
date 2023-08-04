%matplotlib qt5
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
w = 2 * np.pi  # Angular frequency
n_points = 12  # Number of points
angles = np.arange(n_points) * 15  # Angles for each point (in degrees)

# Convert angles from degrees to radians
angles_rad = np.radians(angles)

def animate(frame):
    plt.clf()
    ax = plt.gca()
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_aspect('equal')

    # Calculate the x and y positions for each point
    # These two equations are derived in the note
    x = np.cos(angles_rad) * np.cos(w * frame - angles_rad)
    y = np.sin(angles_rad) * np.cos(w * frame - angles_rad)

    # Plot the points
    ax.scatter(x, y, color='blue', marker='o')

    # Draw unit circle
    circle = plt.Circle((0, 0), 1, color='black', fill=False)
    ax.add_artist(circle)

    # Draw diameters
    for angle_rad in angles_rad:
        dx = [0, np.cos(angle_rad)]
        dy = [0, np.sin(angle_rad)]
        ax.plot(dx, dy, color='gray', linestyle='dashed')

fig = plt.figure()
animation = FuncAnimation(fig, animate, frames=np.linspace(0, 2*np.pi/w, 100), interval=50)

plt.show()
