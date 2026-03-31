# Section 3: Waves — Solutions

---

## 1. Wave Properties

Given:
* Frequency of the sound wave, $f = 440\ \text{Hz}$
* Speed of sound in air, $v_{\text{air}} = 343\ \text{m/s}$
* Speed of sound in water, $v_{\text{water}} = 1482\ \text{m/s}$

The relationship between wave speed, frequency, and wavelength is given by the wave equation:

$$
v = \lambda f
$$

From this, we can solve for the wavelength $\lambda$:

$$
\lambda = \frac{v}{f}
$$

### Wavelength in air

Substitute the values for air:

$$
\lambda_{\text{air}} = \frac{343\ \text{m/s}}{440\ \text{Hz}}
$$

$$
\boxed{\lambda_{\text{air}} \approx 0.780\ \text{m}}
$$

### Wavelength in water

Substitute the values for water:

$$
\lambda_{\text{water}} = \frac{1482\ \text{m/s}}{440\ \text{Hz}}
$$

$$
\boxed{\lambda_{\text{water}} \approx 3.368\ \text{m}}
$$

---

## 2. String Harmonics

Given:
* Length of the guitar string, $L = 64\ \text{cm} = 0.64\ \text{m}$
* Fundamental frequency, $f_1 = 330\ \text{Hz}$

### Mode of vibration

The fundamental frequency (first harmonic) features exactly one antinode between the two fixed ends. This means the string length $L$ corresponds to exactly half of a wavelength:

$$
L = \frac{\lambda_1}{2}
$$

Thus, the wavelength of the fundamental mode is:

$$
\lambda_1 = 2L = 2(0.64\ \text{m}) = 1.28\ \text{m}
$$

### Speed of the wave

Using the wave speed equation $v = \lambda f$:

$$
v = \lambda_1 f_1 = (1.28\ \text{m})(330\ \text{Hz})
$$

$$
\boxed{v = 422.4\ \text{m/s}}
$$

---

## 3. Superposition Principle

Given the two traveling waves:

$$
y_1(x, t) = A \sin(kx - \omega t)
$$
$$
y_2(x, t) = A \sin(kx + \omega t)
$$

### Equation of the resulting standing wave

According to the superposition principle, the resulting wave displacement is the sum of the individual displacements:

$$
y(x, t) = y_1(x, t) + y_2(x, t) = A \sin(kx - \omega t) + A \sin(kx + \omega t)
$$

We can use the trigonometric identity for the sum of sines:

$$
\sin(\alpha) + \sin(\beta) = 2 \sin\left(\frac{\alpha+\beta}{2}\right) \cos\left(\frac{\alpha-\beta}{2}\right)
$$

Let $\alpha = kx - \omega t$ and $\beta = kx + \omega t$:

$$
\frac{\alpha+\beta}{2} = \frac{(kx - \omega t) + (kx + \omega t)}{2} = kx
$$
$$
\frac{\alpha-\beta}{2} = \frac{(kx - \omega t) - (kx + \omega t)}{2} = -\omega t
$$

Substituting these into the identity gives:

$$
y(x, t) = 2A \sin(kx) \cos(-\omega t)
$$

Since cosine is an even function ($\cos(-\theta) = \cos(\theta)$), the resulting wave equation is:

$$
\boxed{y(x, t) = 2A \sin(kx) \cos(\omega t)}
$$

### Positions of the nodes

Nodes are points where the displacement is always zero, regardless of time $t$. This occurs when the spatial part of the standing wave equation is zero:

$$
\sin(kx) = 0
$$

The sine function is zero when its argument is an integer multiple of $\pi$:

$$
kx = n\pi \quad \text{for } n = 0, \pm 1, \pm 2, \dots
$$

Since the wave number $k$ is related to the wavelength $\lambda$ by $k = \frac{2\pi}{\lambda}$, we can write:

$$
\left(\frac{2\pi}{\lambda}\right) x = n\pi
$$

Solving for $x$ gives the positions of the nodes:

$$
\boxed{x = \frac{n\lambda}{2} \quad \text{where } n = 0, 1, 2, 3, \dots}
$$

---

## 4. Phase Difference

Given:
* Separation distance between two points, $\Delta x = \frac{\lambda}{3}$

The relationship between phase difference $\Delta \phi$ and path length difference $\Delta x$ for a wave is:

$$
\Delta \phi = k \Delta x
$$

Where $k$ is the wave number, $k = \frac{2\pi}{\lambda}$. Substituting $k$ and $\Delta x$ into the equation:

$$
\Delta \phi = \left(\frac{2\pi}{\lambda}\right) \left(\frac{\lambda}{3}\right)
$$

The $\lambda$ terms cancel out:

$$
\Delta \phi = \frac{2\pi}{3}
$$

$$
\boxed{\text{The phase difference is } \frac{2\pi}{3} \text{ radians.}}
$$

---

## 5. Echo Ranging

Given:
* Time taken to hear the echo, $t = 1\ \text{s}$
* Speed of sound in air, $v = 343\ \text{m/s}$

For a person to hear an echo, the sound must travel from the person to the cliff and then back again. If the cliff is at a distance $d$ from the person, the total distance traveled by the sound wave is $2d$.

Using the relationship relating distance, speed, and time ($\text{distance} = \text{speed} \times \text{time}$):

$$
2d = vt
$$

Solving for the distance $d$:

$$
d = \frac{vt}{2}
$$

Substitute the given values:

$$
d = \frac{(343\ \text{m/s})(1\ \text{s})}{2}
$$

$$
\boxed{d = 171.5\ \text{m}}
$$

---

## 6. Wave Equation

Given the wave equation:

$$
y(x,t) = 0.05 \sin(2\pi x - 50\pi t)
$$

The standard form of a traveling wave equation is:

$$
y(x, t) = A \sin(kx - \omega t)
$$

By comparing the given equation with the standard form, we can identify parameters.

### a) Amplitude $A$

The coefficient of the sine function is the amplitude:

$$
\boxed{A = 0.05\ \text{m}}
$$

### b) Wavelength $\lambda$

From the equation, the wave number represents the coefficient of $x$:

$$
k = 2\pi\ \text{rad/m}
$$

Since $k = \frac{2\pi}{\lambda}$, we have:

$$
\frac{2\pi}{\lambda} = 2\pi \implies \lambda = 1\ \text{m}
$$

$$
\boxed{\lambda = 1\ \text{m}}
$$

### c) Frequency $f$

From the equation, the angular frequency represents the coefficient of $t$:

$$
\omega = 50\pi\ \text{rad/s}
$$

Since $\omega = 2\pi f$, we have:

$$
2\pi f = 50\pi \implies f = \frac{50\pi}{2\pi} = 25\ \text{Hz}
$$

$$
\boxed{f = 25\ \text{Hz}}
$$

### d) Wave speed $v$

The wave speed is the product of wavelength and frequency:

$$
v = \lambda f = (1\ \text{m})(25\ \text{Hz})
$$

Alternatively, $v = \frac{\omega}{k} = \frac{50\pi}{2\pi} = 25\ \text{m/s}$.

$$
\boxed{v = 25\ \text{m/s}}
$$

---

## 7. Standing Wave Modes

Given:
* Length of the string, $L = 80\ \text{cm} = 0.8\ \text{m}$
* Number of antinodes, $n = 4$

For a string fixed at both ends, forming a standing wave, the length of the string corresponds to an integer number of half-wavelengths:

$$
L = n \frac{\lambda_n}{2}
$$

Solving for the wavelength $\lambda$:

$$
\lambda_n = \frac{2L}{n}
$$

Substitute the given values for the 4th harmonic ($n = 4$):

$$
\lambda_4 = \frac{2(0.8\ \text{m})}{4} = \frac{1.6}{4} = 0.4\ \text{m}
$$

$$
\boxed{\lambda = 0.4\ \text{m} \text{ or } 40\ \text{cm}}
$$

---

## 8. Waves

A function describes a traveling wave if it is a solution to the one-dimensional linearly partial differential wave equation:

$$
\frac{\partial^2 y}{\partial x^2} = \frac{1}{v^2} \frac{\partial^2 y}{\partial t^2}
$$

In general, D'Alembert's solution implies that any function of the form $f(x \pm vt)$ or $f(kx \pm \omega t)$ is a valid traveling wave, provided it describes a valid physical state.

### a) $y(x,t) = A \cos(kx^2 - \omega t)$

Let's test if this is of the form $f(kx \pm \omega t)$. The argument here is $(kx^2 - \omega t)$. Because of the $x^2$ term, the spatial and temporal parameters cannot be factored into the constant velocity linear parameter relation $(x \pm vt)$. 

If we check the derivatives:
$$
\frac{\partial y}{\partial x} = -2Akx \sin(kx^2 - \omega t)
$$
$$
\frac{\partial^2 y}{\partial x^2} = -2Ak \sin(kx^2 - \omega t) - 4Ak^2x^2 \cos(kx^2 - \omega t)
$$
$$
\frac{\partial^2 y}{\partial t^2} = -A\omega^2 \cos(kx^2 - \omega t)
$$

The second partial derivatives are not proportional linearly. Thus, this doesn't satisfy the wave equation.
**No, it does not describe a traveling wave.**

### b) $y(x,t) = A(x-vt)^2$

This function is explicitly in the form $f(x-vt) = A\cdot u^2$ where $u = x-vt$.
Therefore, it mathematically describes a wave traveling to the right with velocity $v$ without changing shape.

If we check the derivatives:
$$
\frac{\partial^2 y}{\partial x^2} = 2A
$$
$$
\frac{\partial^2 y}{\partial t^2} = 2Av^2
$$
Substituting into the wave equation gives $2A = \frac{1}{v^2}(2Av^2) = 2A$.
It satisfies the wave equation perfectly.
**Yes, it describes a traveling wave.**

### c) $y(x,t) = A \log(x+vt)$

This function is also explicitly in the form $f(x+vt) = A\cdot \log(u)$ where $u = x+vt$.
Therefore, it travels to the left with velocity $v$.

Checking the derivatives:
$$
\frac{\partial^2 y}{\partial x^2} = -\frac{A}{(x+vt)^2}
$$
$$
\frac{\partial^2 y}{\partial t^2} = -\frac{Av^2}{(x+vt)^2}
$$
Substituting into the wave equation gives $-\frac{A}{(x+vt)^2} = \frac{1}{v^2} \left(-\frac{Av^2}{(x+vt)^2}\right)$.
It satisfies the wave equation.
**Yes, it describes a traveling wave.**

---

## 9. Damped oscillator

Given equation for a damped harmonic oscillator:

$$
m \frac{d^2 x}{dt^2} + b \frac{dx}{dt} + k x = 0
$$

Divide by $m$ to get the standard form:

$$
\frac{d^2 x}{dt^2} + 2\gamma \frac{dx}{dt} + \omega_0^2 x = 0
$$

Where $\gamma = \frac{b}{2m}$ is the damping coefficient and $\omega_0 = \sqrt{\frac{k}{m}}$ is the natural angular frequency.

### 1. General solution

We guess a solution of the form $x(t) = e^{rt}$. Substituting this into the differential equation yields the characteristic polynomial:

$$
r^2 + 2\gamma r + \omega_0^2 = 0
$$

The roots are given by the quadratic formula:

$$
r = -\gamma \pm \sqrt{\gamma^2 - \omega_0^2}
$$

The general solution is a linear combination of the solutions corresponding to the two roots:

$$
\boxed{x(t) = C_1 e^{r_1 t} + C_2 e^{r_2 t}}
$$

### 2. Classification of cases

The character of the solution depends heavily on the sign of the term under the square root, $\gamma^2 - \omega_0^2$.

* **Underdamped Case ($\gamma < \omega_0 \implies b^2 < 4mk$):**
  The term $\gamma^2 - \omega_0^2$ is negative, so the roots are complex conjugates: $r = -\gamma \pm i\omega_d$, where $\omega_d = \sqrt{\omega_0^2 - \gamma^2}$ is the damped angular frequency.
  Using Euler's formula, the general solution becomes:
  $$
  x(t) = A e^{-\gamma t} \cos(\omega_d t + \phi)
  $$
  The system oscillates with gradually decreasing amplitude.

* **Critically Damped Case ($\gamma = \omega_0 \implies b^2 = 4mk$):**
  The term $\gamma^2 - \omega_0^2$ is zero. This gives a repeated real root $r = -\gamma$.
  The general solution takes the form:
  $$
  x(t) = (C_1 + C_2 t) e^{-\gamma t}
  $$
  The system returns to equilibrium as rapidly as possible without oscillating.

* **Overdamped Case ($\gamma > \omega_0 \implies b^2 > 4mk$):**
  The term $\gamma^2 - \omega_0^2$ is positive, so the roots $r_1$ and $r_2$ are distinct, real, and negative.
  The general solution is:
  $$
  x(t) = C_1 e^{r_1 t} + C_2 e^{r_2 t}
  $$
  The system returns to equilibrium without oscillating, but more slowly than in the critically damped case.

*(Steps 3 to 6 request the implementation of an interactive HTML animation utilizing Runge-Kutta numerical methods, which is out of the scope of this written PDF solution document).*

---

## 10. Animation: Wave Sources

*(Note: The problem requests the development of an HTML/JS animation canvas. Mathematical context is summarized below).*

The total displacement $u(\vec{r},t)$ at a point $\vec{r}$ at time $t$ produced by a system of point sources is given by the superposition:

$$
u(\vec{r},t) = \sum_{n} \frac{A}{|\vec{r}-\vec{r_n}|^\alpha} \sin(k |\vec{r} - \vec{r_n}| - \omega t)
$$

* For $\alpha = 0$, the wave amplitude does not decrease with distance (approx. for ideal 1D wave).
* For $\alpha = 1$, we retrieve standard spherical waves in 3D.
* For $\alpha = 0.5$, we retrieve an approximation for cylindrical waves in 2D space (like ripples on a pond).

---

## 11. Animation: Two-Slit Interference

*(Note: The problem requests an HTML/JS animation modeling Young's double-slit experiment. Mathematical context is provided below).*

The resultant wave displacement from two coherent point sources at $\vec{r_1}$ and $\vec{r_2}$ is:

$$
u(\vec{r},t) = \frac{A}{R_1} \sin(k R_1 - \omega t) + \frac{A}{R_2} \sin(k R_2 - \omega t)
$$

Where $R_1 = |\vec{r}-\vec{r_1}|$ and $R_2 = |\vec{r}-\vec{r_2}|$.

Using the sum-to-product trigonometric identity:

$$
u(\vec{r}, t) \approx \frac{2A}{R_{\text{avg}}} \cos\left(k \frac{R_1 - R_2}{2}\right) \sin\left(k \frac{R_{\text{avg}}}{2} - \omega t\right)
$$

The envelope $\cos\left(k \frac{R_1 - R_2}{2}\right)$ governs the spatial amplitude, resulting in interference:
* **Constructive interference** (bright fringes) occurs when $k(R_1 - R_2) = 2m\pi \implies R_1 - R_2 = m\lambda$.
* **Destructive interference** (dark fringes) occurs when $k(R_1 - R_2) = (2m+1)\pi \implies R_1 - R_2 = \left(m + \frac{1}{2}\right)\lambda$.