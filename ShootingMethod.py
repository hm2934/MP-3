#Harshit Miglani
#22/17053

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sc

#defining the model
def f(y,x):
    return(y[1],-9.8)

#initial conditions
q=5
z,z1=5,6
y0 = [0, z]
u0 = [0, z1]
xs = np.linspace(0,10,50)
s0 = sc.odeint(f,y0,xs)
sol = s0[:,0][-1]
tol=0.001

#"shooting" for solution
for i in range(1000):
    y0 = [0, z]
    u0 = [0, z1]
    s1 = sc.odeint(f,u0,xs)
    sol2 = s1[:, 0][-1]
    if abs(sol-sol2)<tol:
        break
    z, z1 = z1, z1 + (z1 - z) / (sol2 - sol) * (q - sol2)
    sol = sol2
print(s0)

#plotting
plt.plot(xs, s1[:, 0])
plt.show()
