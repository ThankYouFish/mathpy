import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import integrate

# Declarations
t = np.arange(0., 0.5, 0.01) # t-Array for values on x-Axis
y_0 = 15 # Peak ramp value
t_up = 0.5 # Period length
m = 15/0.4 # Gradient

# Functions
y = np.where(t <= 0.4, m * t, 0) # Create ramp signal from 0 to 0.4
y_eff = math.sqrt(1/t_up * integrate.trapezoid(y**2, t, 0.01)) # y_eff to calculate RMS

# Plotting
plt.plot(t, y, label="Periodische Beschleunigung")
plt.grid(True)
plt.xlabel("t")
plt.ylabel("a")
plt.show()

# Print result
print(f"RMS: {y_eff}")