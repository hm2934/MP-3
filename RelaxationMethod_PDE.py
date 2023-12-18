#Harshit Miglani
#22/17053
#references:
#http://mikeskiba.com/laplaces-equation-and-relaxation/
#https://github.com/lukepolson/youtube_channel/blob/main/Python%20Metaphysics%20Series/vid31.ipynb
#https://www.codeproject.com/Articles/1087025/Using-Python-to-Solve-Computational-Physics-Proble
#PDF's in the PDF folder

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

# Set maximum iteration
maxIter = 5000

# Set Dimension and delta
lenX = lenY = 100 #we set it rectangular
V = np.zeros((lenX, lenY), float)
delta = 1

#set inner box voltage to 10
inner_volt = 100
V[(lenX//4) - 1:(3*lenX//4) - 1, (lenX//4) - 1:(3*lenX//4) - 1] = inner_volt
X, Y = np.meshgrid(np.arange(0, lenX), np.arange(0, lenY))

#iterating using relaxation method
print("Please wait for a moment")
for iteration in range(0, maxIter):
    for i in range(1, lenX-1, delta):
        for j in range(1, lenY-1, delta):
            V[i, j] = 0.25 * (V[i+1][j] + V[i-1][j] + V[i][j+1] + V[i][j-1])
    V[(lenX//4) - 1:(3*lenX//4) - 1, (lenX//4) - 1:(3*lenX//4) - 1] = inner_volt

print("Iteration finished")

#plotting
Z = V[X, Y]
fig = plt.figure(1)
ax = plt.axes(projection='3d')
ax.plot_wireframe(X, Y, Z, alpha=0.3, color='#FF0066')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Potential')
cset = ax.contour(X, Y, Z, 60, alpha = 0.8)
ax.clabel(cset, fontsize=9, inline=1,)
plt.show()
