#Harshit Miglani
#22/17053

import numpy as np
import matplotlib.pyplot as plt
def f(a,b):
    return a
def euler(x,y,xf,h):
    xl=[];yl=[]
    while x<xf:
        f1 = f(x, y)
        yl.append(y)
        xl.append(x)
        x = x + h
        y = y + h * f1
    return xl,yl,yl[-1]
s=euler(0,1,5,0.1)
print(s[2])
plt.plot(s[0],s[1], label = 'euler')
x=np.linspace(0,5,100)
y=np.array(1)
y=[1+i**2/2 for i in x]
plt.plot(x,y)
plt.show()
