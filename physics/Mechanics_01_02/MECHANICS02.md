# Section 2: Mechanics II — Solutions

---

## 1. Gravitational Dependence

For a simple pendulum,

$$
T = 2\pi\sqrt{\frac{L}{g}}
$$

For fixed length $L$, the period is proportional to $1/\sqrt{g}$.

### Period on the Moon

Given $T_E = 4\ \text{s}$ on Earth and $g_M = g_E/6$ on the Moon,

$$
\frac{T_M}{T_E} = \sqrt{\frac{g_E}{g_M}} = \sqrt{\frac{g_E}{g_E/6}} = \sqrt{6}
$$

Thus,

$$
T_M = 4\sqrt{6} \approx 9.80\ \text{s}
$$

### Length for a 1-second pendulum on Earth

Set $T=1\ \text{s}$ and solve for $L$:

$$
L = g\left(\frac{T}{2\pi}\right)^2
$$

Using $g=9.81\ \text{m/s}^2$,

$$
L = 9.81\left(\frac{1}{2\pi}\right)^2 \approx 0.248\ \text{m}
$$

So,

$$
\boxed{T_{\text{Moon}} \approx 9.80\ \text{s}, \qquad L \approx 0.248\ \text{m}}
$$

---

## 2. Harmonic Motion

Given

$$
x(t)=0.2\cos(10\pi t)
$$

This is simple harmonic motion of the form

$$
x(t)=A\cos(\omega t)
$$

so

$$
A=0.2\ \text{m}, \qquad \omega=10\pi\ \text{rad/s}
$$

For a mass-spring system,

$$
\omega = \sqrt{\frac{k}{m}}
$$

Hence,

$$
k = m\omega^2 = 10(10\pi)^2 = 1000\pi^2\ \text{N/m}
$$

Numerically,

$$
k \approx 9869.6\ \text{N/m}
$$

The total mechanical energy is

$$
E = \frac{1}{2}kA^2
$$

$$
E = \frac{1}{2}(1000\pi^2)(0.2)^2 = 20\pi^2\ \text{J}
$$

$$
E \approx 197.4\ \text{J}
$$

Therefore,

$$
\boxed{k = 1000\pi^2\ \text{N/m} \approx 9869.6\ \text{N/m}}
$$

$$
\boxed{E = 20\pi^2\ \text{J} \approx 197.4\ \text{J}}
$$

---

## 3. Conservation of Energy

The pendulum is released from rest at angle $\theta=15^\circ$ with length $L=1.0\ \text{m}$.

The loss of gravitational potential energy becomes kinetic energy at the bottom:

$$
mgL(1-\cos\theta)=\frac{1}{2}mv^2
$$

Mass cancels, so

$$
v = \sqrt{2gL(1-\cos\theta)}
$$

Substitute values:

$$
v = \sqrt{2(9.81)(1.0)(1-\cos 15^\circ)} \approx 0.818\ \text{m/s}
$$

So,

$$
\boxed{v \approx 0.818\ \text{m/s}}
$$

---

## 4. Energy & Momentum

### Speed of the 0.5 kg block at the bottom

From energy conservation,

$$
mgh = \frac{1}{2}mv^2
$$

Thus,

$$
v = \sqrt{2gh} = \sqrt{2(9.81)(3.0)} \approx 7.67\ \text{m/s}
$$

### Perfectly inelastic collision

The block sticks to a $1.5\ \text{kg}$ block at rest, so linear momentum is conserved:

$$
m_1v_1 + m_2v_2 = (m_1+m_2)V
$$

With $m_1=0.5$, $v_1=7.67$, $m_2=1.5$, $v_2=0$,

$$
V = \frac{0.5\cdot 7.67}{0.5+1.5} \approx 1.92\ \text{m/s}
$$

Therefore,

$$
\boxed{V \approx 1.92\ \text{m/s}}
$$

---

## 5. Inelastic Collision

Use conservation of momentum:

$$
m_1v_1 + m_2v_2 = (m_1+m_2)V
$$

Given

$$
m_1=70\ \text{kg}, \quad v_1=3\ \text{m/s}, \quad m_2=140\ \text{kg}, \quad v_2=0
$$

Then

$$
V = \frac{70\cdot 3}{70+140} = \frac{210}{210} = 1\ \text{m/s}
$$

So,

$$
\boxed{V = 1\ \text{m/s}}
$$

### Is kinetic energy conserved?

Initial kinetic energy:

$$
K_i = \frac{1}{2}(70)(3^2)=315\ \text{J}
$$

Final kinetic energy:

$$
K_f = \frac{1}{2}(210)(1^2)=105\ \text{J}
$$

Since $K_f \ne K_i$, kinetic energy is not conserved.

$$
\boxed{\text{No, kinetic energy is not conserved.}}
$$

The missing mechanical energy is transformed into heat, sound, and deformation during the inelastic collision.

---

## 6. Energy Dissipation

If the ball loses 30% of its mechanical energy after each bounce, then it keeps 70% of its energy.

Since gravitational potential energy is proportional to height,

$$
h_{n+1}=0.7h_n
$$

Starting from $h_0=2.0\ \text{m}$:

After the first bounce,

$$
h_1 = 0.7(2.0)=1.4\ \text{m}
$$

After the second bounce,

$$
h_2 = 0.7(1.4)=0.98\ \text{m}
$$

Therefore,

$$
\boxed{h_2=0.98\ \text{m}}
$$

---

## 7. Dynamics with Friction

We consider the lower $10\ \text{kg}$ block.

### Friction from the top block

The $5\ \text{kg}$ block is tied to the wall, so the lower block slides under it. The kinetic friction magnitude between the blocks is

$$
f_{12} = \mu_k N_{12} = 0.2(5g) = 0.2(5)(9.81)=9.81\ \text{N}
$$

This acts opposite the motion of the lower block.

### Friction with the ground

The lower block supports both masses, so the normal force from the ground is

$$
N_g = (10+5)g = 15g
$$

Hence the ground friction is

$$
f_g = \mu_k N_g = 0.2(15)(9.81)=29.43\ \text{N}
$$

### Net force on the 10 kg block

$$
F_{\text{net}} = 45 - 9.81 - 29.43 = 5.76\ \text{N}
$$

Thus,

$$
a = \frac{F_{\text{net}}}{10} = \frac{5.76}{10} = 0.576\ \text{m/s}^2
$$

So,

$$
\boxed{a \approx 0.576\ \text{m/s}^2}
$$

---

## 8. Work of a Variable Force

Given

$$
F(x)=-kx
$$

### Equation of motion and solution

Newton's second law gives

$$
m\frac{d^2x}{dt^2}=-kx
$$

or

$$
\frac{d^2x}{dt^2}+\frac{k}{m}x=0
$$

This is the equation of simple harmonic motion. Its general solution is

$$
x(t)=A\cos(\omega t)+B\sin(\omega t)
$$

where

$$
\omega = \sqrt{\frac{k}{m}}
$$

### Work done from $0$ to $x_0$

The work done by the force is

$$
W = \int_0^{x_0} F(x)\,dx = \int_0^{x_0} (-kx)\,dx
$$

$$
W = -k\left[\frac{x^2}{2}\right]_0^{x_0} = -\frac{1}{2}kx_0^2
$$

Thus,

$$
\boxed{W = -\frac{1}{2}kx_0^2}
$$

### Interpretation as potential energy

For a conservative force,

$$
W = -\Delta U
$$

Choosing $U(0)=0$, we obtain

$$
U(x)=\frac{1}{2}kx^2
$$

So,

$$
\boxed{U(x)=\frac{1}{2}kx^2}
$$

### Verify $F = -\frac{dU}{dx}$

Differentiate $U(x)$:

$$
\frac{dU}{dx}=kx
$$

Therefore,

$$
F = -\frac{dU}{dx} = -kx
$$

which matches the given force.

### Graphs of $F(x)$ and $U(x)$

- $F(x)=-kx$ is a straight line through the origin with negative slope.
- $U(x)=\frac{1}{2}kx^2$ is an upward-opening parabola.

Example Python code:

```python
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
```

---

## 9. Vertical Throw with Drag

We solve

$$
m\frac{dv}{dt} = -mg-kv
$$

with $v(0)=v_0$ and $x(0)=10$.

### Analytical solution for velocity

Rewrite as

$$
\frac{dv}{dt}+\frac{k}{m}v=-g
$$

This linear differential equation has solution

$$
v(t)=\left(v_0+\frac{mg}{k}\right)e^{-kt/m}-\frac{mg}{k}
$$

### Position as a function of time

Integrating $v(t)$,

$$
x(t)=10+\frac{m}{k}\left(v_0+\frac{mg}{k}\right)(1-e^{-kt/m})-\frac{mg}{k}t
$$

### Maximum height

At the highest point, $v(t_*)=0$:

$$
\left(v_0+\frac{mg}{k}\right)e^{-kt_*/m}-\frac{mg}{k}=0
$$

So,

$$
t_* = \frac{m}{k}\ln\left(1+\frac{kv_0}{mg}\right)
$$

Substitute into $x(t)$:

$$
x_{\max}=10+\frac{mv_0}{k}-\frac{m^2g}{k^2}\ln\left(1+\frac{kv_0}{mg}\right)
$$

### Comparison with no drag

If $k=0$, then

$$
v(t)=v_0-gt
$$

and the maximum height is

$$
x_{\max}^{(0)}=10+\frac{v_0^2}{2g}
$$

Since drag removes energy, we always have

$$
x_{\max} < x_{\max}^{(0)}
$$

### Numerical simulation in Python

```python
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
```

---

## 10. Force Field and Power

Given

$$
x=5t^2-t, \qquad y=2t^3, \qquad z=-3t+2
$$

and mass $m=0.5\ \text{kg}$.

### Velocity

$$
\vec v(t)=\left(\frac{dx}{dt},\frac{dy}{dt},\frac{dz}{dt}\right)=(10t-1,\ 6t^2,\ -3)
$$

### Momentum

$$
\vec p(t)=m\vec v(t)=0.5(10t-1,\ 6t^2,\ -3)
$$

$$
\vec p(t)=(5t-0.5,\ 3t^2,\ -1.5)
$$

### Acceleration

$$
\vec a(t)=\left(10,\ 12t,\ 0\right)
$$

### Force

$$
\vec F(t)=m\vec a(t)=0.5(10,\ 12t,\ 0)=(5,\ 6t,\ 0)
$$

### Power

Power is

$$
P(t)=\vec F\cdot\vec v
$$

Thus,

$$
P(t)=5(10t-1)+(6t)(6t^2)+0(-3)
$$

$$
P(t)=50t-5+36t^3
$$

So,

$$
\boxed{\vec v(t)=(10t-1,\ 6t^2,\ -3)}
$$

$$
\boxed{\vec p(t)=(5t-0.5,\ 3t^2,\ -1.5)}
$$

$$
\boxed{\vec a(t)=(10,\ 12t,\ 0)}
$$

$$
\boxed{\vec F(t)=(5,\ 6t,\ 0)}
$$

$$
\boxed{P(t)=36t^3+50t-5}
$$

---

## 11. Dynamics with a Time-Dependent Force

Given

$$
\vec F(t)=(15t,\ 3t-12,\ -6t^2)
$$

and mass $m=3\ \text{kg}$.

### Acceleration

From Newton's second law,

$$
\vec a(t)=\frac{\vec F}{m}=(5t,\ t-4,\ -2t^2)
$$

### Velocity

Integrate each component and use $\vec v(0)=(2,0,1)$:

$$
v_x(t)=\int 5t\,dt = \frac{5}{2}t^2 + C_x
$$

Since $v_x(0)=2$, $C_x=2$, so

$$
v_x(t)=\frac{5}{2}t^2+2
$$

Similarly,

$$
v_y(t)=\int (t-4)\,dt = \frac{1}{2}t^2-4t+C_y
$$

Using $v_y(0)=0$, $C_y=0$:

$$
v_y(t)=\frac{1}{2}t^2-4t
$$

And,

$$
v_z(t)=\int (-2t^2)\,dt = -\frac{2}{3}t^3+C_z
$$

Using $v_z(0)=1$, $C_z=1$:

$$
v_z(t)=-\frac{2}{3}t^3+1
$$

Therefore,

$$
\boxed{\vec v(t)=\left(\frac{5}{2}t^2+2,\ \frac{1}{2}t^2-4t,\ -\frac{2}{3}t^3+1\right)}
$$

### Position

Integrate again and use $\vec r(0)=(5,2,-3)$.

For $x$:

$$
x(t)=\int \left(\frac{5}{2}t^2+2\right)dt = \frac{5}{6}t^3+2t+C_1
$$

With $x(0)=5$, $C_1=5$:

$$
x(t)=\frac{5}{6}t^3+2t+5
$$

For $y$:

$$
y(t)=\int \left(\frac{1}{2}t^2-4t\right)dt = \frac{1}{6}t^3-2t^2+C_2
$$

With $y(0)=2$, $C_2=2$:

$$
y(t)=\frac{1}{6}t^3-2t^2+2
$$

For $z$:

$$
z(t)=\int \left(-\frac{2}{3}t^3+1\right)dt = -\frac{1}{6}t^4+t+C_3
$$

With $z(0)=-3$, $C_3=-3$:

$$
z(t)=-\frac{1}{6}t^4+t-3
$$

Thus,

$$
\boxed{\vec r(t)=\left(\frac{5}{6}t^3+2t+5,\ \frac{1}{6}t^3-2t^2+2,\ -\frac{1}{6}t^4+t-3\right)}
$$

---

## 12. Work and Energy with a Constant Force

Given

$$
\vec F=(6,2)\ \text{N}, \qquad m=2\ \text{kg}
$$

with initial data

$$
\vec v(0)=(1,-1), \qquad \vec r(0)=(0,0)
$$

### Acceleration

$$
\vec a(t)=\frac{\vec F}{m}=(3,1)
$$

So,

$$
\boxed{\vec a(t)=(3,1)}
$$

### Velocity

Integrating,

$$
\vec v(t)=(1,-1)+(3,1)t=(1+3t,\ -1+t)
$$

Thus,

$$
\boxed{\vec v(t)=(1+3t,\ -1+t)}
$$

### Position

Integrate velocity:

$$
x(t)=\int (1+3t)dt = t+\frac{3}{2}t^2
$$

$$
y(t)=\int (-1+t)dt = -t+\frac{1}{2}t^2
$$

Using $\vec r(0)=(0,0)$, we get

$$
\boxed{\vec r(t)=\left(t+\frac{3}{2}t^2,\ -t+\frac{1}{2}t^2\right)}
$$

### Trajectory

The motion is parabolic in the plane. A parametric plot of $x(t),y(t)$ gives the trajectory.

Example Python code:

```python
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
```

### Work done by the force at $t=3\ \text{s}$

The displacement from the origin at $t=3$ is

$$
\vec r(3)=\left(3+\frac{3}{2}\cdot 9,\ -3+\frac{1}{2}\cdot 9\right)=(16.5,1.5)
$$

Work done:

$$
W = \vec F\cdot \Delta \vec r = (6,2)\cdot (16.5,1.5)
$$

$$
W = 6(16.5)+2(1.5)=99+3=102\ \text{J}
$$

Thus,

$$
\boxed{W(0\to 3\ \text{s})=102\ \text{J}}
$$

### Work-energy theorem check

Initial kinetic energy:

$$
K_i = \frac{1}{2}m|\vec v(0)|^2 = \frac{1}{2}(2)(1^2+(-1)^2)=2\ \text{J}
$$

At $t=3$,

$$
\vec v(3)=(10,2)
$$

so

$$
K_f = \frac{1}{2}(2)(10^2+2^2)=104\ \text{J}
$$

Hence,

$$
\Delta K = K_f-K_i = 104-2=102\ \text{J}
$$

which agrees with the work found above.

$$
\boxed{W = \Delta K}
$$
