# Solutions: Section 6 - Circuits

## 1. Series and Parallel Circuit
- **Series:** $R_{eq} = R_1 + R_2 + R_3 = 15 + 30 + 50 = 95\,\Omega$
  $I_{series} = \frac{V}{R_{eq}} = \frac{12}{95} \approx 0.126\text{ A}$
- **Parallel:** $\frac{1}{R_{eq}} = \frac{1}{15} + \frac{1}{30} + \frac{1}{50} = \frac{10+5+3}{150} = \frac{18}{150} \Rightarrow R_{eq} = \frac{150}{18} \approx 8.33\,\Omega$
  $I_{parallel} = 12 \cdot \frac{18}{150} = 1.44\text{ A}$

## 2. Resistors
Using exactly three $1\,\Omega$ resistors, there are four possible unique equivalent resistances:
1. **Three in series:** $1 + 1 + 1 = 3\,\Omega$
2. **Three in parallel:** $(\frac{1}{1} + \frac{1}{1} + \frac{1}{1})^{-1} = \frac{1}{3} \approx 0.33\,\Omega$
3. **Two in series, parallel with third:** $(\frac{1}{1+1} + \frac{1}{1})^{-1} = (\frac{1}{2} + 1)^{-1} = \frac{2}{3} \approx 0.67\,\Omega$
4. **Two in parallel, series with third:** $(\frac{1}{1} + \frac{1}{1})^{-1} + 1 = 0.5 + 1 = 1.5\,\Omega$

**Unique values:** $1/3\,\Omega,\ 2/3\,\Omega,\ 1.5\,\Omega,\ 3\,\Omega$.

## 3 & 4. Mixed Circuits
*(Requires analyzing the provided circuit diagrams `image-r1.png` and `image-r2.png`, which are missing here.)*

## 5 & 6. Kirchhoff's Laws
*(Requires analyzing the provided circuit diagrams `image-k1.png` and `image-k2.png`, which are missing here.)*

## 7. Capacitors in Parallel
- $C_{eq} = C_1 + C_2 = 4\,\mu\text{F} + 6\,\mu\text{F} = 10\,\mu\text{F}$
- **Total charge:** $Q = C_{eq}V = 10\,\mu\text{F} \cdot 10\text{ V} = 100\,\mu\text{C}$
- **Total energy:** $E = \frac{1}{2} C_{eq} V^2 = \frac{1}{2} \cdot 10\,\mu\text{F} \cdot (10\text{ V})^2 = 500\,\mu\text{J}$

## 8. AC Voltage Equation
By Ohm's Law $V(t) = I(t)R$:
$V(t) = 50 \cdot 2 \sin(120\pi t) = 100 \sin(120\pi t)\text{ V}$

## 9. Current
Current is the derivative of charge with respect to time $I(t) = \frac{dQ(t)}{dt}$:
$I(t) = \frac{d}{dt}(5t^2 + 5) = 10t$
At $t = 3\text{ s}$, $I(3) = 10(3) = 30\text{ A}$

## 10. Average Current
$I_{avg} = \frac{\Delta Q}{\Delta t} = \frac{30\text{ C}}{2 \times 10^{-3}\text{ s}} = 15,000\text{ A}$

## 11. Power & Energy
- **Power dissipated:** $P = \frac{V^2}{R} = \frac{50^2}{100} = \frac{2500}{100} = 25\text{ W}$ ($25\text{ J/s}$)
- **Energy consumed in 5 minutes:** $E = P \cdot t = 25\text{ W} \cdot (5 \cdot 60\text{ s}) = 25 \cdot 300 = 7500\text{ J}$

## 12. Transformer Currents
For an ideal transformer, $\frac{V_s}{V_p} = \frac{N_s}{N_p}$:
- **Secondary Voltage:** $V_s = 120 \cdot (\frac{200}{1000}) = 120 \cdot 0.2 = 24\text{ V}$ (AC)
- **Primary Current:** Because $P_p = P_s \Rightarrow I_p V_p = I_s V_s \Rightarrow \frac{I_p}{I_s} = \frac{N_s}{N_p}$:
  $I_p = 3 \cdot (\frac{200}{1000}) = 3 \cdot 0.2 = 0.6\text{ A}$

## 13. Transformer Ratio
$\frac{N_s}{N_p} = \frac{V_s}{V_p} \Rightarrow N_s = N_p \cdot \frac{V_s}{V_p}$
$N_s = 400 \cdot \frac{9.0}{120} = 400 \cdot 0.075 = 30\text{ turns}$

## 14. RLC Circuit
By Kirchhoff's Loop Law:
$V(t) = V_L + V_R + V_C = L \frac{d^2q}{dt^2} + R \frac{dq}{dt} + \frac{1}{C}q$
In terms of current ($I = \frac{dq}{dt}$):
$L \frac{dI}{dt} + RI + \frac{1}{C}\int I dt = V(t)$

**Analogies to damped harmonic oscillator:** $m \frac{d^2x}{dt^2} + b \frac{dx}{dt} + kx = F(t)$
- **Charge ($q$)** $\leftrightarrow$ Position ($x$)
- **Current ($I$)** $\leftrightarrow$ Velocity ($v$)
- **Inductance ($L$)** $\leftrightarrow$ Mass ($m$)
- **Resistance ($R$)** $\leftrightarrow$ Damping constant ($b$)
- **Inverse capacitance (1/$C$)** $\leftrightarrow$ Spring constant ($k$)
- **Voltage ($V(t)$)** $\leftrightarrow$ External driving force ($F(t)$)

## 15. Resistor Cube

**Step 1: Setup and Symmetry Analysis**
Imagine a total current $I$ entering the cube at one corner (Node A) and leaving at the diagonally opposite corner (Node B). Because all 12 resistors on the edges are identical (resistance $R$), the cube is perfectly symmetrical with respect to the main diagonal.

---

**Step 2: First Current Split**
At Node A, the current $I$ has three identical outgoing edges. Due to symmetry, the current must split equally into these three paths. 
- Current in each of the 3 edges leaving Node A: $I_1 = \frac{I}{3}$

---

**Step 3: Second Current Split**
Follow one of those paths to the next junction (a "first-layer" node). From this node, there are two forward paths leading towards the exit. Because the network remains symmetrical looking toward Node B, the current splits equally again.
- Current in each of the 6 middle edges: $I_2 = \frac{I_1}{2} = \frac{I}{6}$

---

**Step 4: Current Recombination**
At the junctions just before the exit (the "second-layer" nodes), two edges coming from the middle layer converge. 
- Current entering each of these 3 nodes: $I_3 = 2 \times I_2 = 2 \times \frac{I}{6} = \frac{I}{3}$
These three currents then combine at Node B to give the total outgoing current $I$.

---

**Step 5: Calculating the Total Voltage Drop**
To find the equivalent resistance, we calculate the total voltage drop $V_{AB}$ along any path from Node A to Node B. A shortest path consists of exactly 3 edges (one from each of the splits above). Let's calculate the voltage drop along one such path using Ohm's law ($V = IR$):
- Voltage drop across first edge: $V_1 = I_1 R = \left(\frac{I}{3}\right) R$
- Voltage drop across second edge: $V_2 = I_2 R = \left(\frac{I}{6}\right) R$
- Voltage drop across third edge: $V_3 = I_3 R = \left(\frac{I}{3}\right) R$

Total voltage drop: 
$V_{AB} = V_1 + V_2 + V_3$
$V_{AB} = \frac{I}{3}R + \frac{I}{6}R + \frac{I}{3}R = \left(\frac{2}{6} + \frac{1}{6} + \frac{2}{6}\right) IR = \frac{5}{6} IR$

---

**Step 6: Final Equivalent Resistance**
By definition, the equivalent resistance $R_{eq}$ is the ratio of the total voltage drop to the total current.
$R_{eq} = \frac{V_{AB}}{I} = \frac{\frac{5}{6} IR}{I} = \frac{5}{6}R$

---
