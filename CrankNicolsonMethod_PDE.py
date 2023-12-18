#Harshit Miglani
#22/17053
#references:
#https://youtu.be/lgEOBBNtjiI?feature=shared
#https://youtu.be/6-2Wzs0sXd8?feature=shared
#PDF's in PDF folder

import numpy as np
import matplotlib.pyplot as plt


L = 100
n = 100
T0 = 50
T1s = 100
T2s = 0
dx = L/n
alpha = 110
time = 10
dt = 0.5 * dx**2 / alpha


x = np.linspace(dx/2, L-dx/2, n)

T = np.ones(n)*T0
dTdt = np.empty(n)

t = np.arange(0, time, dt)

fig, axis = plt.subplots()
pcm = axis.pcolormesh([T], cmap=plt.cm.jet, vmin=0, vmax=100)
plt.colorbar(pcm, ax=axis)
axis.set_ylim([-2, 3])

for j in t:
    for i in range(1, n-1):
        dTdt[i] = alpha*(-(T[i]-T[i-1])/dx**2+(T[i+1]-T[i])/dx**2)
    dTdt[0] = alpha*(-(T[0]-T1s)/dx**2+(T[1]-T[0])/dx**2)
    dTdt[n-1] = alpha*(-(T[n-1]-T[n-2])/dx**2+(T2s-T[n-1])/dx**2)
    T = T + dTdt*dt

    # Updating the plot
    pcm.set_array([T])
    axis.set_title("Distribution at t: {:.3f} [s].".format(j))
    plt.pause(0.01)
plt.show()
