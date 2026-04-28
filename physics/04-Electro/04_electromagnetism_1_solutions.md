# Section 4: Electromagnetism I - Solutions

## 1. Coulomb's Law
Since four equal charges of $+1.0\text{ C}$ are placed at the corners of a square, the electric field at the center of the square is zero due to symmetry. All diagonal electric forces acting on a charge placed at the center will cancel out completely.
**Magnitude**: $0\text{ N}$
**Direction**: None

## 2. Electric Potential
The distance $r$ from the corners of a square of side $a = 1.0\text{ m}$ to its center is $r = \frac{a}{\sqrt{2}} \approx 0.707\text{ m}$.
The electric potential $V$ at the center is the scalar sum of the potentials from each charge:
$$ V = k \sum \frac{q_i}{r} = \frac{k}{r} (q_1 + q_2 + q_3 + q_4) $$
$$ V = \frac{8.99 \times 10^9}{1/\sqrt{2}} (1 - 2 + 3 - 4) = 8.99 \times 10^9 \cdot \sqrt{2} \cdot (-2) \approx -2.54 \times 10^{10}\text{ V} $$

## 3. Electrostatic Equilibrium
For the charge $q_3$ to be in equilibrium, the net force on it must be zero. Let $x$ be the distance from $q_1 = +4\text{ C}$.
$$ F_{13} = F_{23} \Rightarrow k\frac{q_1 q_3}{x^2} = k\frac{q_2 q_3}{(2 - x)^2} $$
$$ \frac{4}{x^2} = \frac{9}{(2 - x)^2} $$
Taking the square root of both sides:
$$ \frac{2}{x} = \frac{3}{2 - x} \Rightarrow 4 - 2x = 3x \Rightarrow 5x = 4 \Rightarrow x = 0.8\text{ m} $$
The equilibrium position is $0.8\text{ m}$ from the $q_1 = +4\text{ C}$ charge.

## 4. Force Comparison
Electric force $F_e = k \frac{e^2}{r^2} \approx \frac{(8.99 \times 10^9)(1.6 \times 10^{-19})^2}{(5.3 \times 10^{-11})^2} \approx 8.2 \times 10^{-8}\text{ N}$.
Gravitational force $F_g = G \frac{m_e m_p}{r^2} \approx \frac{(6.67 \times 10^{-11})(9.11 \times 10^{-31})(1.67 \times 10^{-27})}{(5.3 \times 10^{-11})^2} \approx 3.6 \times 10^{-47}\text{ N}$.
Ratio: $\frac{F_e}{F_g} \approx 2.3 \times 10^{39}$.

## 5. Field Levitation
For levitation, the electric force must balance the gravitational force: $qE = mg$.
$$ E = \frac{mg}{q} = \frac{(1.67 \times 10^{-27}\text{ kg})(9.8\text{ m/s}^2)}{1.6 \times 10^{-19}\text{ C}} \approx 1.02 \times 10^{-7}\text{ V/m} $$

## 6. Field at a point from a system of charges
1. $\vec{E}(0, y) = \frac{kq}{(a^2+y^2)^{3/2}} (-a \hat{i} + 3y \hat{j})$
   $\vec{E}(x, 0)$ depends on the region. Between the charges ($-a < x < a$), $E_x = k \left( \frac{q}{(x+a)^2} - \frac{2q}{(x-a)^2} \right)$.
2. $E_x = 0$ when $\frac{1}{(x+a)^2} = \frac{2}{(x-a)^2}$, giving $x = (-3 + 2\sqrt{2})a \approx -0.17a$.
3. With $a=0.2\text{m}$, $y=0.3\text{m}$, $q=2\mu\text{C}$: $E_x \approx -7.7 \times 10^4\text{ V/m}$, $E_y \approx 3.46 \times 10^5\text{ V/m}$
4. For $y \gg a$, $(a^2+y^2)^{3/2} \approx y^3$. Total field is approximately $\vec E \approx \frac{3kq}{y^2} \hat j$, which is the far-field behavior.

## 7. Cyclotron Motion
Kinetic energy acquired: $E_k = qV = (1.6 \times 10^{-19}\text{ C})(5000\text{ V}) = 8 \times 10^{-16}\text{ J}$.
Velocity $v = \sqrt{\frac{2E_k}{m}} \approx 4.19 \times 10^7\text{ m/s}$.
Radius $r = \frac{mv}{qB} = \frac{(9.11 \times 10^{-31})(4.19 \times 10^7)}{(1.6 \times 10^{-19})(0.1)} \approx 2.38 \times 10^{-3}\text{ m} = 2.38\text{ mm}$.

## 8. Lorentz Force
$$ F = qvB\sin(90^\circ) = (2 \times 10^{-19}\text{ C})(10^6\text{ m/s})(0.5\text{ T})(1) = 1.0 \times 10^{-13}\text{ N} $$

## 9. Vector Lorentz Force
Magnetic force $\vec{F} = q(\vec{v} \times \vec{B})$.
Cross product $\vec{v} \times \vec{B} = (2\hat{i} - 4\hat{j} + \hat{k}) \times (\hat{i} + 2\hat{j} - \hat{k}) = (2\hat{i} + 3\hat{j} + 8\hat{k})$.
Magnitude $|\vec{v} \times \vec{B}| = \sqrt{2^2 + 3^2 + 8^2} = \sqrt{77} \approx 8.77\text{ T}\cdot\text{m/s}$.
Magnitude of force $F = (1.6 \times 10^{-19}\text{ C})(\sqrt{77}) \approx 1.40 \times 10^{-18}\text{ N}$.

## 10. Lorentz Force acting on Wire
To calculate the magnetic force on a straight current-carrying wire, we use the formula:

$$F = I \cdot L \cdot B \cdot \sin(\theta)$$

Where:
* **$F$** is the magnetic force (in Newtons, N)
* **$I$** is the current = 10 A
* **$L$** is the length of the wire = 2.0 m
* **$B$** is the magnetic field strength = 0.5 T
* **$\theta$** is the angle between the wire and the magnetic field

First, let's find the maximum possible force (when $\sin(\theta) = 1$):
$$F_{max} = 10 \text{ A} \cdot 2.0 \text{ m} \cdot 0.5 \text{ T} = 10 \text{ N}$$

Now, we can calculate the force for each specific angle by multiplying this maximum force by $\sin(\theta)$:

**a) Angle is 90°**
The wire is perpendicular to the magnetic field.
$$F = 10 \cdot \sin(90^\circ)$$
$$F = 10 \cdot 1 = 10 \text{ N}$$

**b) Angle is 45°**
$$F = 10 \cdot \sin(45^\circ)$$
$$F = 10 \cdot \left(\frac{\sqrt{2}}{2}\right)$$
$$F = 5\sqrt{2} \approx 7.07 \text{ N}$$

**c) Angle is 0°**
The wire is parallel to the magnetic field.
$$F = 10 \cdot \sin(0^\circ)$$
$$F = 10 \cdot 0 = 0 \text{ N}$$

When the wire is parallel to the magnetic field (0° or 180°), it experiences zero magnetic force. It experiences the maximum force when it is exactly perpendicular (90°).