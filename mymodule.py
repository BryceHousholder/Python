#This is a remake of my ECE105 MATLAB Assignment

import numpy as np
import matplotlib.pyplot as plt
import math
# define parameters
c_1 = 0.032
c_2 = 0.164
k = 8.65
m = 1.23
t = np.arange(0,17.5,0.05)
Omega = math.sqrt(k/m)
# calculate KE in Joules
KE = (1/2) * m * np.square(-c_1 * Omega * np.sin(Omega * t) + c_2 * Omega * np.cos(Omega * t))
# calculates the position of the spring in cm
y = c_1 * np.cos(Omega * t) + c_2 * np.sin(Omega * t)
# plot
plt.subplot(1,2,1)
plt.plot(t,y)
plt.title('Spring Positions')
plt.xlabel('Time [Seconds]')
plt.ylabel('Position of Spring [cm]')
plt.subplot(1,2,2)
plt.plot(t,KE)
plt.title('Kinetic Energy of Mass')
plt.xlabel('Time [seconds]')
plt.ylabel('Kinetic Energy [Joules]')
plt.tight_layout()
plt.show()