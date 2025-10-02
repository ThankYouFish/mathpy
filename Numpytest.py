import numpy as np
import matplotlib.pyplot as plt

# Generate data
x = np.linspace(0, 10, 100)   # 100 points between 0 and 10
y1 = np.sin(x)                 # sine function
y2 = np.cos(x)                 # cosine function
y3 = np.tan(x)

# Plot
plt.plot(x, y1, label="sin(x)")
plt.plot(x, y2, label="cos(x)")
plt.plot(x, y3, label="tan(x)")
plt.title("Multiple Functions")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()