#Harshit Miglani
#22/17053

import numpy as np
import matplotlib.pyplot as plt

# Define the complex functions
def f_zplane(z):
    return z

def f_square(z):
    return z**2

def f_four(z):
    return z**4

def f_inv(z):
    return 1/z

def f_exp(z):
    return np.exp(z)

def f_root(z):
    return np.sqrt(z)

# Define a grid of complex numbers in the z-plane
x = np.linspace(-2, 2, 400)
y = np.linspace(-2, 2, 400)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y

# Z plane
Z_plane = f_zplane(Z)

# Apply the functions to the grid to map to the w-plane
Z_squared = f_square(Z)

Z_four = f_four(Z)

Z_inv = f_inv(Z)

Z_exp = f_exp(Z)

Z_root = f_root(Z)

# Create subplots to display the results
fig, axes = plt.subplots(3,2, figsize=(10,10))

# Plot the  z
axes[0,0].imshow(np.angle(Z), extent=(x.min(), x.max(), y.min(), y.max()), cmap='hsv', origin='lower')
axes[0,0].set_title('Mapping of z')

# Plot the mapping of z^2
axes[0,1].imshow(np.angle(Z_squared), extent=(x.min(), x.max(), y.min(), y.max()), cmap='hsv', origin='lower')
axes[0,1].set_title('Mapping of z^2')

# Plot the mapping of z^4
axes[1,0].imshow(np.angle(Z_four), extent=(x.min(), x.max(), y.min(), y.max()), cmap='hsv', origin='lower')
axes[1,0].set_title('Mapping of z^4')

# Plot the mapping of 1/z
axes[1,1].imshow(np.angle(Z_inv), extent=(x.min(), x.max(), y.min(), y.max()), cmap='hsv', origin='lower')
axes[1,1].set_title('Mapping of 1/z')

# Plot the mapping of e^z
axes[2,0].imshow(np.angle(Z_exp), extent=(x.min(), x.max(), y.min(), y.max()), cmap='hsv', origin='lower')
axes[2,0].set_title('Mapping of e^z')

# Plot the mapping of z^(1/2)
axes[2,1].imshow(np.angle(Z_root), extent=(x.min(), x.max(), y.min(), y.max()), cmap='hsv', origin='lower')
axes[2,1].set_title('Mapping of z^(1/2)')

plt.show()
