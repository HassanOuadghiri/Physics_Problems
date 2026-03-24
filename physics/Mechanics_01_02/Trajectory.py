import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 3, 400)
x = t + 1.5 * t**2
y = -t + 0.5 * t**2

plt.figure(figsize=(5, 5))
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axis("equal")
plt.show()