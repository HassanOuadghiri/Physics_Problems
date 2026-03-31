# Section 3: Waves

## 1. Wave Properties

A sound wave in air has a frequency of 440 Hz. If the speed of sound in air is 343 m/s, what is its wavelength? What is its wavelength in water, where the speed of sound is 1482 m/s?

## 2. String Harmonics

A guitar string is 64 cm long and has a fundamental frequency (one antinode) of 330 Hz. What is the speed of the wave on this string?

## 3. Superposition Principle

Two waves are described by the equations $y_1(x, t) = A \sin(kx - \omega t)$ and $y_2(x, t) = A \sin(kx + \omega t)$. What is the equation of the resulting standing wave? Identify the positions of the nodes.

## 4. Phase Difference

What is the phase difference in radians between two points on a wave that are separated by a distance of $\lambda/3$? 

## 5. Echo Ranging

A person shouts towards a cliff and hears the echo 1 seconds later. How far away is the cliff? (Speed of sound in air is 343 m/s).

## 6. Wave Equation

A wave is described by the equation $y(x,t) = 0.05 \sin(2\pi x - 50\pi t)$, where x and y are in meters and t is in seconds. Determine the waves':

a) Amplitude $A$.

b) Wavelength $\lambda$.

c) Frequency $f$.

d) Wave speed $v$.

## 7. Standing Wave Modes

A standing wave with four antinodes is produced on a string of length L = 80 cm. What is the wavelength of this wave?

## 8. Waves

Which of the following functions can describe a traveling wave? Hint: check if it satisfies the wave equation 

$$\frac{\partial^2 y}{\partial x^2} = \frac{1}{v^2} \frac{\partial^2 y}{\partial t^2}$$

a) $y(x,t) = A \cos(kx^2 - \omega t)$

b) $y(x,t) = A(x-vt)^2$

c) $y(x,t) = A \log(x+vt)$

## 9. Damped oscillator

For the given equation describing a damped harmonic oscillator:

$$
m \frac{d^2 x}{dt^2} + b \frac{dx}{dt} + k x = 0
$$

make interactive HTML animation with a slider for the parameter $b$ to show the behavior of the system in the underdamped, critically damped, and overdamped cases. Include graphs of $x(t)$ and the phase portrait for each case.

1. Write down the general solution.
2. Present the classification of cases: underdamped, critically damped, overdamped.
3. Solve the equation numerically (RK4).
4. Investigate the effect of parameter $b$.
5. Generate the graph of $x(t)$.
6. Generate the phase portrait.

## 10. Animation: Wave Sources

Write an HTML animation in which it is possible to place dots that will serve as sources of waves described by the equation:

$$
u(\vec{r},t) = \frac{A}{|\vec{r}-\vec{r_0}|^\alpha} \sin(k |\vec{r} - \vec{r_0}| - \omega t)
$$

where $\vec{r_0}$ is the position of the dot, and $\alpha$ is a parameter that can be set within the range $[0, 2]$. The animation should show the superposition of waves from all dots.


## 11. Animation: Two-Slit Interference

Write an HTML animation simulating Young's experiment, in which two slits act as point sources of coherent waves. The displacement of the resultant wave is the sum of partial waves described by the formula:

$$
u(\vec{r},t) = \frac{A}{|\vec{r}-\vec{r_1}|} \sin(k |\vec{r} - \vec{r_1}| - \omega t) + \frac{A}{|\vec{r}-\vec{r_2}|} \sin(k |\vec{r} - \vec{r_2}| - \omega t)
$$

where $\vec{r_1}$ and $\vec{r_2}$ are the position vectors of the slits. The user should be able to change the distance between the slits $d = |\vec{r_1} - \vec{r_2}|$ and the wavelength $\lambda$. The animation should visualize the resulting interference pattern in real time.