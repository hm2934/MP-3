#Harshit Miglani
#22/17053

import numpy as np
import matplotlib.pyplot as plt

#boundary conditions
xi = 0
xf = 10
yi = 0
yf = 100
n = 50
y = np.zeros(n+1)
y[0] = yi
y[n] = yf
x, h = np.linspace(xi, xf, n+1, retstep=True)
f1, ax1 = plt.subplots(1, 3, figsize=(20, 5))

#iterating over finite differences
for j in range(2001):
    for i in range(1, n):
        y[i] = (y[i+1] + y[i-1])/2 + 9.8*h**2/2
    if j % 40 == 0 and j <= 100:
        ax1[0].plot(x, y, label=str(j))
    if j % 200 == 0 and j <= 500:
        ax1[1].plot(x, y, label=str(j))
    if j % 400 == 0:
        ax1[2].plot(x, y, label=str(j))

#plotting
plt.suptitle("iterative Finite Difference Method")
ax1[0].set_title('k=200')
ax1[1].set_title('k=1000')
ax1[2].set_title('k=2000')
#for i in range(3):
#    ax1[i].grid()
#    ax1[i].legend(loc='best')
f1.tight_layout()
plt.savefig('C:\\Users\\lenovo\\Downloads\\fdiff.png', dpi=1000)
plt.show()
