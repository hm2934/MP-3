#Harshit Miglani
#22/17053
#references:
#https://pythonnumericalmethods.berkeley.edu/notebooks/chapter24.03-Fast-Fourier-Transform.html
#https://pythonnumericalmethods.berkeley.edu/notebooks/chapter24.00-Fourier-Transforms.html
#PDF's in PDF folder

import matplotlib.pyplot as plt
import numpy as np

# sampling rate
sr = 256
# sampling interval
ts = 1.0/sr
t = np.arange(-1,1,ts)
f = np.exp(-t**2)
plt.plot(t, f, 'r')
plt.ylabel('Amplitude')
plt.show()


def FFT(x):
    """
    A recursive implementation of
    the 1D Cooley-Tukey FFT, the
    input should have a length of
    power of 2.
    """
    N = len(x)

    if N == 1:
        return x
    else:
        X_even = FFT(x[::2])
        X_odd = FFT(x[1::2])
        factor = \
            np.exp(-2j * np.pi * np.arange(N) / N)

        X = np.concatenate( \
            [X_even + factor[:int(N / 2)] * X_odd,
             X_even + factor[int(N / 2):] * X_odd])
        return X

X=FFT(f)
# calculate the frequency
N = len(X)
n = np.arange(N)
T = N/sr
freq = n/T
plt.stem(freq, abs(X), 'b', markerfmt=" ", basefmt="-b")
plt.xlabel('Freq (Hz)')
plt.ylabel('FFT Amplitude')
plt.show()

# Get the one-sided specturm
n_oneside = N//2
# get the one side frequency
f_oneside = freq[:n_oneside]

# normalize the amplitude
X_oneside =X[:n_oneside]/n_oneside
plt.stem(f_oneside, abs(X_oneside), 'b', markerfmt=" ", basefmt="-b")
plt.xlabel('Freq (Hz)')
plt.ylabel('Normalized FFT Amplitude')
plt.xlim(-1, 11)
plt.show()
