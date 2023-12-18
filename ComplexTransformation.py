#Harshit Miglani
#22/17053

from math import *

#defining the complex number
z = 2+3j

#translation
t_fact = 1+2j #translation factor
z_translated = z + t_fact

#scaling
s_fact = 3 #scaling factor
z_scaled = z * s_fact

#rotation
angle_deg = 60
angle_rad = radians(angle_deg)
r_fact = complex(cos(angle_rad),sin(angle_rad)) #factor of rotation
z_rotated = z * r_fact

#reflection
rf_fact = complex(0,-1) #reflection faction
z_reflected = z * rf_fact

print('Orignal Complex Number :',z)
print('Translated Complex Number :',z_translated)
print('Scaled Complex Number :',z_scaled)
print('Rotated Complex Number :',z_rotated)
print('Reflected Complex Number :',z_reflected)
