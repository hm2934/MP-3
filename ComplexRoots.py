#Harshit Miglani
#22/17053

import matplotlib.pyplot as plt
from math import *
import cmath as cm

#n for nth root of unity
n = int(input('Enter n:'))
root = []
for k in range(n):
    i = (2*pi*k)/n
    r = cm.rect(1,i)
    root.append(r)
print(root)
x = [i.real for i in root]
y = [i.imag for i in root]

#plotting the roots
figure, axes = plt.subplots()
cc = plt.Circle((0,0),1,fill=False)
axes.set_aspect(1)
axes.add_artist(cc)
plt.scatter(x,y)
plt.xlim(-1.5,1.5)
plt.ylim(-1.5,1.5)
plt.grid()
plt.title('nth roots of unity')
plt.show()
