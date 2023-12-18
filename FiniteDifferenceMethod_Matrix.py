#Harshit Miglani
#22/17053

import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as lin

n=int(input('No. of rows in matrix:'))
a=np.zeros([n,n])
b=np.zeros(n)
h=0.1
ya = 1
yb=20
x=np.linspace(0,10,n+2)
for i in range(n):
    if i == 0:
        b[i] = (-10 * h ** 2) - ya
    elif i == (n - 1):
        b[i] = (-10 * h ** 2) - yb
    else:
        b[i] = -10 * h ** 2
    for j in range(n):
        if i==j:
            a[i][j] = -2
            if (i-1) >= 0:
                a[i][j-1]=1
            if (i+1) < n:
                a[i][j+1]=1
        else:
            continue
print(a,b)
c=lin.solve(a,b)
print(c,x)
c=np.insert(c,0,ya)
c=np.append(c,yb)
print(c)
plt.plot(x,c)
plt.show()
