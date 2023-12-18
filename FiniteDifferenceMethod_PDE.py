#Harshit Miglani
#22/17053

#references:
#https://www.youtube.com/watch?v=CXOrkQs4WYo
#PDF's in PDF folder

import numpy as np
import matplotlib.pyplot as plt


# Defining our problem

a = 110
length = 100 #mm
time = 10 #seconds
nodes = 51

# Initialization

dx = length / nodes
dt = 0.5 * dx**2 / a
t_nodes = int(time/dt)
u = np.zeros(nodes) + 40 # Plate is initially as 40 degres C

# Boundary Conditions
u[0] = 100
u[26] = 50
u[-1] = 0

# Visualizing with a plot
fig, axis = plt.subplots()
pcm = axis.pcolormesh([u], cmap=plt.cm.jet, vmin=0, vmax=100)
plt.colorbar(pcm, ax=axis)
axis.set_ylim([-2, 3])

# Simulating
counter = 0
while counter < time :
    w = u.copy()
    for i in range(1, nodes - 1):
        if i==26:
            continue
        u[i] = dt * a * (w[i - 1] - 2 * w[i] + w[i + 1]) / dx ** 2 + w[i]
    counter += dt
    print("t: {:.3f} [s], Average temperature: {:.2f} Celcius".format(counter, np.average(u)))
    # Updating the plot
    pcm.set_array([u])
    axis.set_title("Distribution at t: {:.3f} [s].".format(counter))
    plt.pause(0.01)

plt.show()
