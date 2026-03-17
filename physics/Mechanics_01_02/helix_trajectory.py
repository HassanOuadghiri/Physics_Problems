"""
Trajectory of point M: r(t) = (a*cos(wt), b*sin(wt), b*t)

Special cases explored:
  1. a == b  ->  circular helix
  2. a != b  ->  elliptical helix  (default)
  3. b == 0  ->  planar ellipse  (no rise in z)
  4. w == 0  ->  straight vertical line  (x=a, y=0, z=b*t)
"""

import numpy as np
import matplotlib.pyplot as plt

# ── parameters ────────────────────────────────────────────────────────────────
CASES = [
    {"label": "Elliptical helix  (a=4, b=2, ω=1.2)", "a": 4.0, "b": 2.0, "w": 1.2},
    {"label": "Circular helix    (a=b=3, ω=1.2)",      "a": 3.0, "b": 3.0, "w": 1.2},
    {"label": "Planar ellipse    (b=0, a=3, ω=1.5)",   "a": 3.0, "b": 0.0, "w": 1.5},
    {"label": "Straight line     (ω=0, a=2, b=1)",     "a": 2.0, "b": 1.0, "w": 0.0},
]

T0 = 6 * np.pi          # total time (enough for ~3 full turns for typical ω)
N  = 2000               # number of time samples


def compute_path(a, b, w, t0=T0, n=N):
    """Return (t, x, y, z, arc_length) arrays."""
    t = np.linspace(0, t0, n)
    x = a * np.cos(w * t)
    y = b * np.sin(w * t)
    z = b * t

    # arc-length via numerical integration of |v(t)|
    # v = (-a*w*sin(wt), b*w*cos(wt), b)
    vx = -a * w * np.sin(w * t)
    vy =  b * w * np.cos(w * t)
    vz =  np.full_like(t, b)
    speed = np.sqrt(vx**2 + vy**2 + vz**2)
    dt = t[1] - t[0]
    arc = np.cumsum(speed) * dt       # running arc-length

    return t, x, y, z, arc


# ── figure ────────────────────────────────────────────────────────────────────
fig = plt.figure(figsize=(14, 10))
fig.suptitle(
    r"Trajectory of $\vec{r}(t)=(a\cos\omega t,\ b\sin\omega t,\ bt)$",
    fontsize=14, fontweight="bold"
)

for idx, case in enumerate(CASES):
    a, b, w = case["a"], case["b"], case["w"]
    t, x, y, z, arc = compute_path(a, b, w)

    ax = fig.add_subplot(2, 2, idx + 1, projection="3d")
    sc = ax.scatter(x, y, z, c=t, cmap="plasma", s=2, linewidths=0)
    ax.plot(x, y, z, color="steelblue", linewidth=0.8, alpha=0.5)

    # mark start and end
    ax.scatter(*[x[0]], *[y[0]], *[z[0]], color="green", s=60, zorder=5, label="t=0")
    ax.scatter(*[x[-1]], *[y[-1]], *[z[-1]], color="red",   s=60, zorder=5, label=f"t=t₀")

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_title(case["label"], fontsize=9)
    ax.legend(fontsize=8)

    total_arc = arc[-1]
    ax.text2D(0.02, 0.02, f"arc ≈ {total_arc:.2f}", transform=ax.transAxes, fontsize=8)

plt.colorbar(sc, ax=fig.axes, shrink=0.5, label="time t")
plt.tight_layout()
plt.savefig(
    r"d:\Sem2_Vizja\physics\Mechanics_01_02\helix_trajectory.png",
    dpi=150, bbox_inches="tight"
)
print("Saved helix_trajectory.png")
plt.show()
