import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import integrate

t = np.arange(0., 0.5, 0.01) #t-Array für meine Werte auf x-Achse

y_0 = 15
t_up = 0.5
m = 15/0.4
y = np.where(t <= 0.4, m * t, 0)
y_eff = math.sqrt(1/t_up * integrate.trapezoid(y**2, t, 0.01))

plt.plot(t, y, label="Periodische Beschleunigung")
plt.grid(True)
plt.xlabel("t")
plt.ylabel("a")
plt.show()

print(f"RMS: {y_eff}")