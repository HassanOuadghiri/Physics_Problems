import numpy as np
import matplotlib.pyplot as plt

m = 1.0
g = 9.81
k = 0.4
v0 = 20.0
x0 = 10.0
dt = 0.001
t_max = 5.0

t = np.arange(0, t_max + dt, dt)
v = np.zeros_like(t)
x = np.zeros_like(t)
v[0] = v0
x[0] = x0

for i in range(len(t) - 1):
    a = -g - (k / m) * v[i]
    v[i + 1] = v[i] + a * dt
    x[i + 1] = x[i] + v[i] * dt

plt.figure(figsize=(8, 4))
plt.plot(t, x, label="x(t)")
plt.plot(t, v, label="v(t)")
plt.xlabel("t")
plt.legend()
plt.grid(True)
plt.show()