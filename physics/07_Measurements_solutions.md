# Solutions to Section 7: Measurements

## 1. Propagation of Error I

**Step 1: Identify the given values.**
- Radius $r = 6.20 \text{ cm}$
- Uncertainty in radius $\Delta r = 0.05 \text{ cm}$

**Step 2: Calculate the volume.**
- The formula for the volume of a sphere is: $V = \frac{4}{3} \pi r^3$
- Substitute the value of $r$: $V = \frac{4}{3} \pi (6.20)^3 \approx 998.3 \text{ cm}^3$

**Step 3: Calculate the relative and absolute uncertainty in the volume.**
- Since $r$ is raised to the power of 3, we multiply its relative uncertainty by 3:
  $\frac{\Delta V}{V} = 3 \frac{\Delta r}{r}$
- To find the absolute uncertainty ($\Delta V$), rearrange the formula:
  $\Delta V = 3 \times \left(\frac{\Delta r}{r}\right) \times V$
- Substitute the values: $\Delta V = 3 \times \left(\frac{0.05}{6.20}\right) \times 998.3 \approx 24.2 \text{ cm}^3$

**Step 4: State the final result.**
- Combine the calculated volume and uncertainty: $V = (998.3 \pm 24.2) \text{ cm}^3$

---

## 2. Propagation of Error II

**Step 1: Identify the given values.**
- Length $L = 15.3 \text{ cm}$, Uncertainty $\Delta L = 0.1 \text{ cm}$
- Width $W = 8.4 \text{ cm}$, Uncertainty $\Delta W = 0.1 \text{ cm}$

**Step 2: Calculate the area.**
- The formula for the area of a rectangle is: $A = L \times W$
- Substitute the values: $A = 15.3 \times 8.4 = 128.52 \text{ cm}^2$

**Step 3: Calculate the relative and absolute uncertainty in the area.**
- For multiplication, we add the relative uncertainties of each measurement:
  $\frac{\Delta A}{A} = \frac{\Delta L}{L} + \frac{\Delta W}{W}$
- To find the absolute uncertainty, multiply by the area $A$:
  $\Delta A = A \times \left(\frac{\Delta L}{L} + \frac{\Delta W}{W}\right)$
- Substitute the values: $\Delta A = 128.52 \times \left(\frac{0.1}{15.3} + \frac{0.1}{8.4}\right) \approx 2.37 \text{ cm}^2$ (round to 2.4)

**Step 4: State the final result.**
- Combine the calculated area and uncertainty: $A = (128.5 \pm 2.4) \text{ cm}^2$

---

## 3. Propagation of Error III

**Step 1: Identify the given values.**
- Voltage $V = 10.0 \text{ V}$, Uncertainty $\Delta V = 0.2 \text{ V}$
- Current $I = 2.00 \text{ A}$, Uncertainty $\Delta I = 0.05 \text{ A}$

**Step 2: Calculate the resistance.**
- Using Ohm's Law: $R = \frac{V}{I}$
- Substitute the values: $R = \frac{10.0}{2.00} = 5.00 \ \Omega$

**Step 3: Calculate the relative and absolute uncertainty in the resistance.**
- For division, just like multiplication, we add the relative uncertainties:
  $\frac{\Delta R}{R} = \frac{\Delta V}{V} + \frac{\Delta I}{I}$
- To find the absolute uncertainty, multiply by the resistance $R$:
  $\Delta R = R \times \left(\frac{\Delta V}{V} + \frac{\Delta I}{I}\right)$
- Substitute the values: $\Delta R = 5.00 \times \left(\frac{0.2}{10.0} + \frac{0.05}{2.00}\right) = 0.225 \ \Omega \approx 0.23 \ \Omega$

**Step 4: State the final result.**
- Combine the calculated resistance and uncertainty: $R = (5.00 \pm 0.23) \ \Omega$

---

## 4. Relative Uncertainty

**Step 1: Identify the given values.**
- Reading speed $v = 60 \text{ km/h}$
- Relative uncertainty = $5\%$ or $0.05$

**Step 2: Calculate the absolute uncertainty.**
- Multiply the reading speed by the relative uncertainty:
  $\Delta v = 60 \times 0.05 = 3 \text{ km/h}$

**Step 3: Determine the range.**
- The actual speed can be lower or higher by the absolute uncertainty.
- Range = $[60 - 3, 60 + 3] \text{ km/h} = [57, 63] \text{ km/h}$

---

## 5. Percentage Calculation

**Step 1: Identify the given values.**
- Measurement $t = 5.45 \text{ s}$
- Absolute uncertainty $\Delta t = 0.22 \text{ s}$

**Step 2: Calculate the percentage uncertainty.**
- Divide the absolute uncertainty by the measurement, then multiply by $100\%$:
  $\text{Percentage Uncertainty} = \left(\frac{\Delta t}{t}\right) \times 100\%$
- Substitute the values: $\left(\frac{0.22}{5.45}\right) \times 100\% \approx 4.04\%$

---

## 6. Instrument Precision

**Step 1: Identify the reading and the position of the last digit.**
- Reading $= 25.4^\circ\text{C}$
- The last digit is in the tenths place, meaning the smallest unit it can measure is $0.1^\circ\text{C}$.

**Step 2: Calculate the absolute uncertainty.**
- The problem states uncertainty is half the value of the last digit.
- $\text{Absolute Uncertainty} = \frac{0.1}{2} = 0.05^\circ\text{C}$

---

## 7. Standard Deviation

**Step 1: Analyze all 11 scores.**
- Data ($N=11$): 88, 92, 79, 85, 95, 81, 86, 90, 83, 77, 89
- Calculate the Mean ($\bar{x}$): Sum all scores and divide by $N$.
  $\bar{x} = \frac{88+92+79+85+95+81+86+90+83+77+89}{11} = \frac{945}{11} \approx 85.91$
- Calculate the Standard Deviation ($\sigma$): Find the squared differences from the mean, sum them, divide by $N-1$, and take the square root.
  $\sigma = \sqrt{\frac{(88-85.91)^2 + (92-85.91)^2 + \dots}{10}} \approx 5.58$

**Step 2: Analyze the remaining 9 scores.**
- Remove highest (95) and lowest (77). Remaining data ($N=9$): 88, 92, 79, 85, 81, 86, 90, 83, 89
- Calculate the New Mean:
  $\bar{x} = \frac{773}{9} \approx 85.89$
- Calculate the New Standard Deviation:
  $\sigma \approx \sqrt{\frac{148.89}{8}} \approx 4.31$

---

## 8. Mass-Spring Measurements

This outlines the steps to perform when you run the simulation:

**Step 1: Perform the measurements.**
- Run the simulation 10 times, each time recording how long it takes for the mass to bounce up and down 10 full times ($t_{10}$).

**Step 2: Determine the mean period.**
- Calculate the average of your 10 total time measurements. Let's call this $t_{10, mean}$.
- To find the time for just *one* oscillation (the period $T$), divide the average by 10:
  $T_{mean} = \frac{t_{10, mean}}{10}$

**Step 3: Calculate the spring constant.**
- We know the period formula is: $T = 2\pi\sqrt{\frac{m}{k}}$
- Rearrange this formula to solve for the spring constant $k$:
  $k = \frac{4\pi^2m}{T^2}$

**Step 4: Calculate the uncertainty.**
- Since we treat the mass as exact ($\Delta m = 0$), the relative uncertainty of $k$ depends only on $T$. Because $T$ is squared in the denominator, multiply its relative uncertainty by 2:
  $\frac{\Delta k}{k} = 2\frac{\Delta T}{T}$

---

## 9. Pendulum Measurements

This outlines the steps to perform when you run the pendulum simulation or real-life experiment:

**Step 1: Perform the measurements.**
- Keep the length ($L$) constant. Time 10 full swings of the pendulum back and forth ($t_{10}$).
- Repeat this 10 separate times and record each combined duration.

**Step 2: Determine the mean period.**
- Calculate the average of your 10 time measurements ($t_{10, mean}$).
- Find the period ($T$, time per one swing) by dividing the average by 10:
  $T_{mean} = \frac{t_{10, mean}}{10}$

**Step 3: Calculate the acceleration due to gravity.**
- The pendulum period formula is: $T = 2\pi\sqrt{\frac{L}{g}}$
- Rearrange to solve for gravity ($g$):
  $g = \frac{4\pi^2L}{T^2}$

**Step 4: Calculate the uncertainty.**
- Treat length $L$ as an exact value ($\Delta L = 0$). Since $T$ is squared, the relative uncertainty of $g$ is twice the relative uncertainty of $T$:
  $\frac{\Delta g}{g} = 2\frac{\Delta T}{T}$

---

## 10. Light Speed Measurement

This outlines how to perform the calculations after doing the microwave experiment:

**Step 1: Identify the wavelength.**
- While the chocolate melts, it forms spots at the "hot spots" (antinodes) of the microwave standing wave.
- The distance between two neighboring hot spots is exactly *half* a wavelength ($d = \frac{\lambda}{2}$).
- Therefore, to find the full wavelength ($\lambda$), multiply your measured distance by 2: $\lambda = 2d$.

**Step 2: Calculate the speed of light.**
- The wave equation is speed = frequency $\times$ wavelength ($c = f \cdot \lambda$).
- The frequency of a typical microwave is $f = 2.45 \text{ GHz}$, which means $2.45 \times 10^9 \text{ Hz}$ (or waves per second).
- Substitute your wavelength to find the measured speed of light:
  $c_{\text{measured}} = (2.45 \times 10^9) \times (2d)$

**Step 3: Calculate the percentage error.**
- Compare your measured speed to the accepted value ($300,000,000 \text{ m/s}$).
- Formula: $\text{Percentage Error} = \frac{|c_{\text{measured}} - 300,000,000|}{300,000,000} \times 100\%$

