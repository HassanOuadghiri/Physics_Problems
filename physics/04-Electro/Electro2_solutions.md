# Section 5: Electromagnetism II - Solutions

## 1. Gauss's Law

The electric flux passing through a closed surface (like the spherical surface) enclosing a charge $q$ is independent of the size of the surface and is given by Gauss's Law:
$$ \Phi_E = \frac{q}{\varepsilon_0} $$
Given $q = +2 \text{ C}$ and the permittivity of free space $\varepsilon_0 \approx 8.854 \times 10^{-12} \text{ F/m}$:
$$ \Phi_E = \frac{2}{8.854 \times 10^{-12}} \approx 2.26 \times 10^{11} \text{ N}\cdot\text{m}^2/\text{C} $$

## 2. Ampere's Law

The magnetic field at a distance $r$ from a long straight wire is $B = \frac{\mu_0 I}{2 \pi r}$.
The point midway between the wires is at a distance $r = \frac{10 \text{ cm}}{2} = 5 \text{ cm} = 0.05 \text{ m}$ from both wires.
Since the currents are in opposite directions, by the right-hand rule, the magnetic fields from both wires point in the **same direction** at the midpoint.
$$ B_\text{total} = B_1 + B_2 = 2 \times \frac{\mu_0 I}{2 \pi r} = \frac{\mu_0 I}{\pi r} $$
With $\mu_0 = 4\pi \times 10^{-7} \text{ T}\cdot\text{m/A}$, $I = 5 \text{ A}$, and $r = 0.05 \text{ m}$:
$$ B_\text{total} = \frac{4\pi \times 10^{-7} \cdot 5}{\pi \cdot 0.05} = \frac{20 \times 10^{-7}}{0.05} = 4 \times 10^{-5} \text{ T} $$
The direction is perpendicular to the plane containing the wires.

## 3. Biot-Savart Law

The magnetic field from a current segment is roughly:
$$ dB = \frac{\mu_0 I \, dl \, \sin\theta}{4 \pi r^2} $$
Given $\theta = 90^\circ$, $I = 3 \text{ A}$, $dl = 0.1 \text{ m}$, and $r = 0.2 \text{ m}$:
$$ B \approx \frac{4\pi \times 10^{-7} \cdot 3 \cdot 0.1 \cdot 1}{4 \pi (0.2)^2} = \frac{10^{-7} \cdot 0.3}{0.04} = 7.5 \times 10^{-7} \text{ T} $$

## 4. Magnetic Torque

The magnetic torque on a current loop is $\tau = N I A B \sin\theta$.
The area $A = 0.10 \text{ m} \times 0.05 \text{ m} = 0.005 \text{ m}^2$. The field is parallel to the plane of the loop, meaning the angle between the area vector (perpendicular to the plane) and the magnetic field is $\theta = 90^\circ$.
$$ \tau = 1 \cdot 2 \text{ A} \cdot 0.005 \text{ m}^2 \cdot 0.3 \text{ T} \cdot \sin(90^\circ) = 0.003 \text{ N}\cdot\text{m} $$

## 5. Energy Stored by charge in a capacitor

Given: $S = 0.02 \text{ m}^2$, $d = 5 \text{ mm} = 0.005 \text{ m}$, $V = 500 \text{ V}$.

1.  **Capacitance $C$:**
    $$ C = \frac{\varepsilon_0 S}{d} = \frac{8.854 \times 10^{-12} \cdot 0.02}{0.005} = 3.54 \times 10^{-11} \text{ F} = 35.4 \text{ pF} $$
2.  **Energy $U$:**
    $$ U = \frac{1}{2} C V^2 = \frac{1}{2} (3.54 \times 10^{-11}) (500)^2 \approx 4.43 \times 10^{-6} \text{ J} $$
3.  **Electric field intensity $E$:**
    $$ E = \frac{V}{d} = \frac{500}{0.005} = 10^5 \text{ V/m} $$
4.  **Force of attraction $F$:**
    $$ F = \frac{\varepsilon_0 S E^2}{2} = \frac{8.854 \times 10^{-12} \cdot 0.02 \cdot (10^5)^2}{2} \approx 8.85 \times 10^{-4} \text{ N} $$

## 6. EM Wave Analysis

Given: $E_y(x,t) = 100 \sin(10^7 x - \omega t) \text{ V/m}$.

*   **Direction of propagation:** Because the phase term is $(kx - \omega t)$, the wave propagates in the **$+x$-direction**.
*   **Wavelength $\lambda$:** The wave number $k = 10^7 \text{ m}^{-1}$. Since $k = \frac{2\pi}{\lambda}$:
    $$ \lambda = \frac{2\pi}{10^7} \approx 6.28 \times 10^{-7} \text{ m} = 628 \text{ nm} $$
*   **Angular frequency $\omega$:** For an EM wave in vacuum, $\frac{\omega}{k} = c \approx 3 \times 10^8 \text{ m/s}$.
    $$ \omega = k c = 10^7 \cdot 3 \times 10^8 = 3 \times 10^{15} \text{ rad/s} $$
*   **Magnetic field component:** The B-field is perpendicular to E ($y$-axis) and propagation ($x$-axis), so it points along the $z$-axis. Its amplitude is $B_0 = \frac{E_0}{c} = \frac{100}{3 \times 10^8} \approx 3.33 \times 10^{-7} \text{ T}$.
    $$ B_z(x,t) = 3.33 \times 10^{-7} \sin(10^7 x - 3 \times 10^{15} t) \text{ T} $$

## 7. Wavelength and Frequency

*   **Color:** A wavelength of $550 \text{ nm}$ corresponds to **yellow-green** in the visible spectrum.
*   **Frequency $f$:**
    $$ f = \frac{c}{\lambda} = \frac{3 \times 10^8}{550 \times 10^{-9}} \approx 5.45 \times 10^{14} \text{ Hz} $$

## 8. EM Spectrum

In order of **increasing wavelength** (decreasing energy):
1. Gamma rays (shortest wavelength)
2. X-rays
3. Ultraviolet
4. Infrared
5. Microwaves
6. Radio waves (longest wavelength)

## 9. Refraction (Snell's Law)

Using Snell's Law $n_1 \sin\theta_1 = n_2 \sin\theta_2$:
$$ 1.00 \sin(30^\circ) = 1.50 \sin\theta_2 $$
$$ 0.5 = 1.50 \sin\theta_2 $$
$$ \sin\theta_2 = \frac{0.5}{1.50} = \frac{1}{3} $$
$$ \theta_2 = \arcsin(1/3) \approx 19.47^\circ $$

## 10. Speed of Light in Media

The speed of light in a medium is $v = \frac{c}{n}$.
$$ v = \frac{3 \times 10^8 \text{ m/s}}{2.42} \approx 1.24 \times 10^8 \text{ m/s} $$