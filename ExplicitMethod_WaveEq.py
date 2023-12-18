#Harshit Miglani
#22/17053

#references:
#https://wiki.seg.org/wiki/Solving_the_wave_equation_in_1D
#https://youtu.be/HKSDBtNqhHk?feature=shared
#https://youtu.be/DiV2lAH80_s?feature=shared
#https://youtu.be/onpYV1EMZRI?feature=shared
#PDF's in PDF folder
import numpy as np
from math import *
import matplotlib.pyplot as plt

dx = 0.01
dt = 0.05
L = 1
r = 1
# make xs

x = np.arange(0,L,dx)

###need three lists - yold, ynow, yfuture
fold = []
fnow = []
fnew = []
for i in range(len(x)):
    fold = fold + [0]
    fnow = fnow + [0]
    fnew = fnew + [0]

A = 1
for i in range(len(x)):
    fold[i] = A * sin(2 * pi * x[i])
    fnow[i] = A * sin(2 * pi * x[i])
    fnew[i] = A * sin(2 * pi * x[i])
    '''
    if x[i]<=L:
      fold[i]=A*sin(2*pi*x[i])
      fnow[i]=A*sin(2*pi*x[i])
  
    else:
      fold[i]=-A*sin(2*pi*x[i])
      fnow[i]=-A*sin(2*pi*x[i])
    '''

# for i in range(len(fold)):
#  f1.plot(x[i],fold[i])
# print(fnew)

t = 0
while t < 5:
    plt.clf()
    fdata = []
    for i in range(1, len(x) - 1):
        fnew[i] = 2 * fnow[i] - fold[i] + r ** 2 * (fnow[i + 1] + fnow[i - 1] - 2 * fnow[i])
    # update old
    for i in range(1, len(x) - 1):
        fold[i] = fnow[i]
    # update new
    for i in range(1, len(x) - 1):
        fnow[i] = fnew[i]
    # graph
    for i in range(len(x)):
        fdata = fdata + [[x[i], fnew[i]]]
    t = t + dt
    plt.figure(1)
    plt.plot(x, fnew)
    plt.axis([0, L, -1.5, 1.5])
    plt.pause(0.01)
plt.show()

print("finished")
# print(fnew)
