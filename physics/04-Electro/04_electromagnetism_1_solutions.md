# Section 4: Electromagnetism I - Solutions

## 1. Coulomb's Law
To calculate the electric force on a charge from multiple other charges, we use the principle of superposition and Coulomb's Law:

$$F = \sum k \cdot \frac{q_i \cdot q_{center}}{r^2}$$

Where:
* **$F$** is the net electric force (in Newtons, N)
* **$k$** is Coulomb's constant $\approx 8.99 \times 10^9 \text{ N}\cdot\text{m}^2/\text{C}^2$
* **$q_{corner}$** are the corner charges = $+1.0 \text{ C}$
* **$q_{center}$** is the center charge = $-2.0 \text{ C}$
* **$r$** is the distance from each corner to the center

First, we calculate the magnitude of force from one corner:
$$F_1 = k \cdot \frac{|+1.0 \cdot -2.0|}{r^2} = k \cdot \frac{2}{r^2}$$

Since four equal charges of $+1.0\text{ C}$ are placed at the corners of a square:
* The distance $r$ from the center to each corner is identical.
* The forces from diagonally opposite charges are equal in magnitude but perfectly opposite in direction.

$$F_{net} = \vec{F}_1 + \vec{F}_2 + \vec{F}_3 + \vec{F}_4$$

All diagonal electric forces acting on a charge placed at the center will cancel out completely:
$$F = 0 \text{ N}$$

When identical charges are placed symmetrically around a central point, the net electric field and the resulting electric force at that center are always zero due to spatial symmetry.

## 2. Electric Potential
To calculate the total electric potential at a point due to multiple point charges, we use the scalar superposition formula:

$$V = k \cdot \sum \frac{q_i}{r}$$

Where:
* **$V$** is the total electric potential (in Volts, V)
* **$k$** is Coulomb's constant $\approx 8.99 \times 10^9 \text{ N}\cdot\text{m}^2/\text{C}^2$
* **$q_1, q_2, q_3, q_4$** are the corner charges = $+1\text{C}, -2\text{C}, +3\text{C}, -4\text{C}$
* **$r$** is the distance from each corner to the center of the square

First, let's find the distance $r$ for a square of side $a = 1.0 \text{ m}$:
$$r = \frac{a}{\sqrt{2}} = \frac{1.0}{\sqrt{2}} \approx 0.707 \text{ m}$$

Now, we substitute the values into the potential sum formula:
$$V = \frac{k}{r} \cdot (q_1 + q_2 + q_3 + q_4)$$
$$V = \frac{8.99 \times 10^9}{1/\sqrt{2}} \cdot (1 - 2 + 3 - 4)$$
$$V = (8.99 \times 10^9 \cdot \sqrt{2}) \cdot (-2)$$
$$V \approx -2.54 \times 10^{10} \text{ V}$$

Unlike electric force or field, electric potential is a scalar quantity, so we can simply add the algebraic values of the potentials from each charge without worrying about vector directions.

## 3. Electrostatic Equilibrium
To find the electrostatic equilibrium position, where the net force on a third charge is zero, we equate the magnitudes of the forces applied by the two other charges:

$$F_{13} = F_{23} \implies k \cdot \frac{q_1 \cdot q_3}{x^2} = k \cdot \frac{q_2 \cdot q_3}{(d - x)^2}$$

Where:
* **$F$** is the electric force
* **$q_1$** is the first charge = $+4 \text{ C}$
* **$q_2$** is the second charge = $+9 \text{ C}$
* **$q_3$** is the test charge = $+1 \text{ C}$
* **$d$** is the total distance between $q_1$ and $q_2$ = $2 \text{ m}$
* **$x$** is the distance from $q_1$ to the equilibrium point

First, we can simplify the equation by canceling out $k$ and $q_3$:
$$\frac{q_1}{x^2} = \frac{q_2}{(2 - x)^2}$$
$$\frac{4}{x^2} = \frac{9}{(2 - x)^2}$$

Now, taking the square root of both sides to solve for $x$:
$$\frac{2}{x} = \frac{3}{2 - x}$$
$$2 \cdot (2 - x) = 3 \cdot x$$
$$4 - 2x = 3x$$
$$5x = 4$$
$$x = 0.8 \text{ m}$$

The equilibrium position is located $0.8 \text{ m}$ away from the $+4 \text{ C}$ charge. If the two main charges have the same sign, the equilibrium point is always located strictly between them, closer to the charge with the smaller magnitude.

## 4. Force Comparison
To compare the electric and gravitational forces between two particles, we evaluate Coulomb's Law and Newton's Law of Universal Gravitation:

$$F_e = k \cdot \frac{q_1 \cdot q_2}{r^2} \quad \text{and} \quad F_g = G \cdot \frac{m_1 \cdot m_2}{r^2}$$

Where:
* **$F_e$**, **$F_g$** are the electric and gravitational forces respectively (in N)
* **$k$** is Coulomb's constant $\approx 8.99 \times 10^9 \text{ N}\cdot\text{m}^2/\text{C}^2$
* **$G$** is the gravitational constant $\approx 6.67 \times 10^{-11} \text{ N}\cdot\text{m}^2/\text{kg}^2$
* **$e$** is the elementary charge $\approx 1.6 \times 10^{-19} \text{ C}$
* **$m_e$** is the electron mass $\approx 9.11 \times 10^{-31} \text{ kg}$
* **$m_p$** is the proton mass $\approx 1.67 \times 10^{-27} \text{ kg}$
* **$r$** is the distance between them $\approx 5.3 \times 10^{-11} \text{ m}$

First, we calculate the electric force:
$$F_e = \frac{(8.99 \times 10^9) \cdot (1.6 \times 10^{-19})^2}{(5.3 \times 10^{-11})^2} \approx 8.2 \times 10^{-8} \text{ N}$$

Next, we calculate the gravitational force:
$$F_g = \frac{(6.67 \times 10^{-11}) \cdot (9.11 \times 10^{-31}) \cdot (1.67 \times 10^{-27})}{(5.3 \times 10^{-11})^2} \approx 3.6 \times 10^{-47} \text{ N}$$

Now, we find the ratio of these forces:
$$\frac{F_e}{F_g} = \frac{8.2 \times 10^{-8}}{3.6 \times 10^{-47}} \approx 2.3 \times 10^{39}$$

The electric force heavily dominates the gravitational force at atomic scales. Gravity is so weak compared to electromagnetism that it is typically entirely ignored in atomic physics.

## 5. Field Levitation
To levitate a particle, the upward electric force must perfectly balance the downward gravitational force:

$$F_e = F_g \implies q \cdot E = m \cdot g$$

Where:
* **$E$** is the electric field strength (in V/m or N/C)
* **$q$** is the charge of the proton $\approx 1.6 \times 10^{-19} \text{ C}$
* **$m$** is the mass of the proton $\approx 1.67 \times 10^{-27} \text{ kg}$
* **$g$** is the gravitational acceleration $\approx 9.8 \text{ m/s}^2$

First, let's rearrange the formula to solve for the electric field $E$:
$$E = \frac{m \cdot g}{q}$$

Now, we plug in the given specific values:
$$E = \frac{(1.67 \times 10^{-27}) \cdot 9.8}{1.6 \times 10^{-19}}$$
$$E \approx 1.02 \times 10^{-7} \text{ V/m}$$

To counter earth's gravity on a tiny particle like a proton, an incredibly small macroscopic electric field is sufficient, showcasing once again the relative strength of the electromagnetic force versus gravity.

## 6. Field at a point from a system of charges
To calculate the total electric field at arbitrary coordinates, we use vector superposition of fields from each charge:

$$\vec{E} = \sum k \cdot \frac{q_i}{r_i^2} \cdot \hat{r}_i$$

Where:
* **$\vec{E}$** is the total electric field vector
* **$k$** is Coulomb's constant
* **$q_1$** is the first charge $= +q$ at $(-a, 0)$
* **$q_2$** is the second charge $= +2q$ at $(a, 0)$

**1. General field definitions:**
On the y-axis $(0, y)$, combining both charges:
$$\vec{E}(0, y) = \frac{kq}{(a^2+y^2)^{3/2}} \cdot (-a \hat{i} + 3y \hat{j})$$
On the x-axis $(x, 0)$ between the charges ($-a < x < a$), the field only has an x-component:
$$E_x = k \cdot \left( \frac{q}{(x+a)^2} - \frac{2q}{(x-a)^2} \right)$$

**2. Condition for zero field:**
Setting $E_x = 0$ along the axis where the field components oppose each other:
$$\frac{1}{(x+a)^2} = \frac{2}{(x-a)^2}$$
$$x = (-3 + 2\sqrt{2}) \cdot a \approx -0.17a$$

**3. Specific calculation:**
Given values: $a = 0.2 \text{ m}$, $y = 0.3 \text{ m}$, $q = 2 \mu\text{C}$ (which means $2 \times 10^{-6} \text{ C}$):
$$E_x \approx -7.7 \times 10^4 \text{ V/m}$$
$$E_y \approx 3.46 \times 10^5 \text{ V/m}$$

**4. Limit $y \gg a$:**
For large distances compared to charge separation, $(a^2+y^2)^{3/2} \approx y^3$. We find the total field:
$$\vec E \approx \frac{k \cdot 3q}{y^2} \hat j$$

From far away, the field acts approximately like a single point charge of magnitude $3q$ representing the net system charge.

## 7. Cyclotron Motion
To calculate the radius of a moving charged particle in a perpendicular magnetic field, we balance the Lorentz force with centripetal force:

$$F_{Lorentz} = F_{centripetal} \implies q \cdot v \cdot B = \frac{m \cdot v^2}{r}$$

Where:
* **$r$** is the radius of the circular path
* **$v$** is the velocity of the particle
* **$V$** is the accelerating potential = $5000 \text{ V}$
* **$B$** is the magnetic field = $0.1 \text{ T}$
* **$m$** is the mass of the electron $\approx 9.11 \times 10^{-31} \text{ kg}$
* **$q$** is the charge of the electron $\approx 1.6 \times 10^{-19} \text{ C}$

First, we determine the velocity the electron gains from the potential $V$:
$$E_k = q \cdot V = (1.6 \times 10^{-19}) \cdot 5000 = 8 \times 10^{-16} \text{ J}$$
$$v = \sqrt{\frac{2 \cdot E_k}{m}} = \sqrt{\frac{2 \cdot (8 \times 10^{-16})}{9.11 \times 10^{-31}}} \approx 4.19 \times 10^7 \text{ m/s}$$

Now, rearrange our initial formula to solve for $r$ and substitute the velocity:
$$r = \frac{m \cdot v}{q \cdot B}$$
$$r = \frac{(9.11 \times 10^{-31}) \cdot (4.19 \times 10^7)}{(1.6 \times 10^{-19}) \cdot 0.1}$$
$$r \approx 2.38 \times 10^{-3} \text{ m} = 2.38 \text{ mm}$$

Magnetic fields do not do work on particles; they only change the direction of velocity, trapping the electron in a stable circular orbit called cyclotron motion.

## 8. Lorentz Force
To calculate the magnitude of the magnetic Lorentz force on a moving charge, we use the formula:

$$F = q \cdot v \cdot B \cdot \sin(\theta)$$

Where:
* **$F$** is the magnetic force (in Newtons, N)
* **$q$** is the charge = $2 \times 10^{-19} \text{ C}$
* **$v$** is the speed = $10^6 \text{ m/s}$
* **$B$** is the magnetic field = $0.5 \text{ T}$
* **$\theta$** is the angle; given as perpendicular, so $\theta = 90^\circ$

First, substitute the given values into the equation:
$$F = (2 \times 10^{-19}) \cdot 10^6 \cdot 0.5 \cdot \sin(90^\circ)$$

Since $\sin(90^\circ) = 1$:
$$F = (10^{-13}) \cdot 1 = 1.0 \times 10^{-13} \text{ N}$$

The maximum macroscopic force happens exactly when the particle interacts completely perpendicular to the field lines.

## 9. Vector Lorentz Force
To calculate the magnetic force on a charge with vector velocity and field components, we use the vector cross product formulation:

$$\vec{F} = q \cdot (\vec{v} \times \vec{B})$$

Where:
* **$\vec{F}$** is the magnetic force vector
* **$q$** is the elementary charge $\approx 1.6 \times 10^{-19} \text{ C}$
* **$\vec{v}$** is the velocity vector $= (2\hat{i} - 4\hat{j} + \hat{k}) \text{ m/s}$
* **$\vec{B}$** is the magnetic field vector $= (\hat{i} + 2\hat{j} - \hat{k}) \text{ T}$

First, let's calculate the cross product $\vec{v} \times \vec{B}$:
$$\vec{v} \times \vec{B} = (2\hat{i} - 4\hat{j} + \hat{k}) \times (\hat{i} + 2\hat{j} - \hat{k})$$
$$\vec{v} \times \vec{B} = (2\hat{i} + 3\hat{j} + 8\hat{k})$$

Next, find the magnitude of this resulting cross product vector:
$$|\vec{v} \times \vec{B}| = \sqrt{2^2 + 3^2 + 8^2} = \sqrt{4 + 9 + 64} = \sqrt{77} \approx 8.77 \text{ T}\cdot\text{m/s}$$

Finally, we calculate the magnitude of the force by multiplying by the proton charge $q$:
$$F = q \cdot |\vec{v} \times \vec{B}|$$
$$F = (1.6 \times 10^{-19}) \cdot 8.77 \approx 1.40 \times 10^{-18} \text{ N}$$

The resulting force vector is always strictly perpendicular to both the initial velocity vector and the magnetic field vector, a principle elegantly captured by the mathematical cross product.

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
