import numpy as np
import matplotlib.pyplot as plt

k = 2
x = np.linspace(-3, 3, 400)
F = -k * x
U = 0.5 * k * x**2

fig, ax = plt.subplots(1, 2, figsize=(10, 4))
ax[0].plot(x, F)
ax[0].axhline(0, color="black", linewidth=0.8)
ax[0].axvline(0, color="black", linewidth=0.8)
ax[0].set_title("Force")
ax[0].set_xlabel("x")
ax[0].set_ylabel("F(x)")

ax[1].plot(x, U)
ax[1].axhline(0, color="black", linewidth=0.8)
ax[1].axvline(0, color="black", linewidth=0.8)
ax[1].set_title("Potential Energy")
ax[1].set_xlabel("x")
ax[1].set_ylabel("U(x)")

plt.tight_layout()
plt.show()