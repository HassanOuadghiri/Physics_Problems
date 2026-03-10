# Section 0: Mathematical Foundations — Solutions

---

## 1. Vector Algebra

**Given:** $\vec{a} = [2, 1, -3]$, $\vec{b} = [4, -2, 1]$

### a) Magnitudes

$$|\vec{a}| = \sqrt{2^2 + 1^2 + (-3)^2} = \sqrt{4 + 1 + 9} = \sqrt{14} \approx 3.742$$

$$|\vec{b}| = \sqrt{4^2 + (-2)^2 + 1^2} = \sqrt{16 + 4 + 1} = \sqrt{21} \approx 4.583$$

### b) Dot Product

$$\vec{a} \cdot \vec{b} = (2)(4) + (1)(-2) + (-3)(1) = 8 - 2 - 3 = 3$$

### c) Cross Product

$$\vec{a} \times \vec{b} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 2 & 1 & -3 \\ 4 & -2 & 1 \end{vmatrix}$$

$$= \hat{i}\bigl(1 \cdot 1 - (-3)(-2)\bigr) - \hat{j}\bigl(2 \cdot 1 - (-3)(4)\bigr) + \hat{k}\bigl(2(-2) - 1 \cdot 4\bigr)$$

$$= \hat{i}(1 - 6) - \hat{j}(2 + 12) + \hat{k}(-4 - 4)$$

$$\boxed{\vec{a} \times \vec{b} = [-5,\ -14,\ -8]}$$

### d) Angle Between the Vectors

$$\cos\theta = \frac{\vec{a} \cdot \vec{b}}{|\vec{a}|\,|\vec{b}|} = \frac{3}{\sqrt{14}\,\sqrt{21}} = \frac{3}{\sqrt{294}} = \frac{3}{7\sqrt{6}}$$

$$\boxed{\theta = \arccos\!\left(\frac{3}{7\sqrt{6}}\right) \approx 1.394 \text{ rad} \approx \frac{4\pi}{9}}$$

---

## 2. Systems of Equations

**Given:**

$$2x + 3y = 12 \quad (1)$$
$$x - y = 1 \quad (2)$$

From equation (2): $x = y + 1$

Substitute into (1):

$$2(y + 1) + 3y = 12$$
$$2y + 2 + 3y = 12$$
$$5y = 10$$

$$\boxed{y = 2, \quad x = 3}$$

**Verification:** $2(3) + 3(2) = 12$ ✓ and $3 - 2 = 1$ ✓

---

## 3. Proportionality

**Given:** $F = G\dfrac{m_1 m_2}{r^2}$, with $r' = 2r$, $m_1' = \dfrac{m_1}{2}$, $m_2' = \dfrac{m_2}{2}$.

$$F' = G\frac{m_1' \, m_2'}{r'^2} = G\frac{\frac{m_1}{2} \cdot \frac{m_2}{2}}{(2r)^2} = G\frac{\frac{m_1 m_2}{4}}{4r^2} = \frac{1}{16}\,G\frac{m_1 m_2}{r^2}$$

$$\boxed{F' = \frac{F}{16}}$$

The gravitational force **decreases by a factor of 16**.

---

## 4. Rearranging Formulas

**Given:** $T = 2\pi\sqrt{\dfrac{L}{g}}$

Square both sides:

$$T^2 = 4\pi^2 \frac{L}{g}$$

Solve for $g$:

$$\boxed{g = \frac{4\pi^2 L}{T^2}}$$

---

## 5. Trigonometry

**Given:** $|\vec{A}| = 15$, $\theta = 60°$

$$A_x = |\vec{A}|\cos\theta = 15\cos(60°) = 15 \times \frac{1}{2}$$

$$\boxed{A_x = 7.5}$$

$$A_y = |\vec{A}|\sin\theta = 15\sin(60°) = 15 \times \frac{\sqrt{3}}{2}$$

$$\boxed{A_y = \frac{15\sqrt{3}}{2} \approx 12.99}$$

---

## 6. Function Analysis

**Given:** $f(x) = 3x^2 - 12x + 7$

Find the critical point by setting the first derivative to zero:

$$f'(x) = 6x - 12 = 0 \implies x = 2$$

Check the second derivative:

$$f''(x) = 6 > 0 \quad \text{(concave up, so it is a minimum)}$$

Evaluate:

$$f(2) = 3(4) - 12(2) + 7 = 12 - 24 + 7 = -5$$

$$\boxed{\text{Local minimum at } (2,\ -5)}$$

---

## 7. Logic & Series (The Fly Problem)

**Key insight:** Instead of tracking each leg of the fly's trip, consider the total time available.

The bicycle reaches the wall in:

$$t = \frac{10 \text{ m}}{1 \text{ m/s}} = 10 \text{ s}$$

During this entire time, the fly is always in motion at $2\text{ m/s}$:

$$d_{\text{fly}} = 2 \text{ m/s} \times 10 \text{ s}$$

$$\boxed{d_{\text{fly}} = 20 \text{ m}}$$

---

## 8. Definite Integrals

**Given:** $\displaystyle\int_0^{\pi} \sin(x)\,dx$

$$\int_0^{\pi} \sin(x)\,dx = \bigl[-\cos(x)\bigr]_0^{\pi} = -\cos(\pi) - \bigl(-\cos(0)\bigr) = -(-1) + 1 = 1 + 1$$

$$\boxed{\int_0^{\pi} \sin(x)\,dx = 2}$$

---

## 9. Optimization Problem

**Given:** Rectangle inscribed under $y = 3 - x^2$ in the first quadrant, with one corner at the origin.

The rectangle has width $x$ and height $y = 3 - x^2$, so:

$$A(x) = x(3 - x^2) = 3x - x^3, \qquad 0 < x < \sqrt{3}$$

Set the derivative to zero:

$$A'(x) = 3 - 3x^2 = 0 \implies x^2 = 1 \implies x = 1$$

Confirm it is a maximum:

$$A''(x) = -6x \implies A''(1) = -6 < 0 \quad \checkmark$$

Dimensions:

$$\boxed{\text{Width } = 1, \quad \text{Height } = 3 - 1^2 = 2, \quad A_{\max} = 2}$$

---

## 10. Infinite Series (The Ant Problem)

The ant's movements cycle through **east, north, west, south** with step sizes $\dfrac{1}{n}$:

| Step $n$ | Direction | Displacement |
|----------|-----------|-------------|
| 1 | East (+x) | 1 |
| 2 | North (+y) | 1/2 |
| 3 | West (−x) | 1/3 |
| 4 | South (−y) | 1/4 |
| 5 | East (+x) | 1/5 |
| 6 | North (+y) | 1/6 |
| ... | ... | ... |

### x-coordinate

$$x = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \cdots = \sum_{k=0}^{\infty} \frac{(-1)^k}{2k+1}$$

This is the **Leibniz formula**:

$$x = \frac{\pi}{4}$$

### y-coordinate

$$y = \frac{1}{2} - \frac{1}{4} + \frac{1}{6} - \frac{1}{8} + \cdots = \frac{1}{2}\sum_{k=1}^{\infty} \frac{(-1)^{k+1}}{k}$$

This is $\frac{1}{2}$ times the **alternating harmonic series**:

$$y = \frac{1}{2}\ln 2$$

### Final Position

$$\boxed{\left(\frac{\pi}{4},\ \frac{\ln 2}{2}\right) \approx (0.785,\ 0.347)}$$
