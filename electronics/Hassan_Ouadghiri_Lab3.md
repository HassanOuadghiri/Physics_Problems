# Measurement Report: Active current circuits - Lab no 3

**Student Name:** Hassan Ouadghiri

## 1. Testing of a power supply system with a half-wave rectifier

**Falstad Link:** https://is.gd/p0V36U

**Table 2:**
| R[kOhm] | C[uF] | U1 (V) | A. (mA) | U2+ (V) | U2- (V) | U3+ (V) | U3- (V) |
|-------|-------|--------|---------|---------|---------|---------|---------|
| 0.1   | 0     | 20     | 15.9    | 5.0     | 0.0     | 15.0    | -20.0   |
| 0.1   | 1     | 20     | 15.9    | 5.0     | 0.0     | 15.0    | -20.0   |

![oscillogram](Capture%20d%E2%80%99%C3%A9cran%202026-04-21%20195330.png)

![oscillogram](Capture%20d%E2%80%99%C3%A9cran%202026-04-21%20195528.png)

**Characteristics:**
- **Operation:** A half-wave rectifier uses a single diode to convert alternating current (AC) into pulsing direct current (DC).
- **Forward Direction Context:** During the positive half of the AC cycle, the diode is forward-biased, allowing current to flow to the load.
- **Reverse Direction Context:** During the negative half of the cycle, the diode becomes reverse-biased, effectively blocking the current. This results in the load receiving power for only half of the input AC cycle.
- **Efficiency:** Since half of the input wave is unused, this setup produces a lower average output voltage and more significant ripple compared to full-wave designs.


## 2. Testing of a power supply system with a full-wave rectifier

**Falstad Link:** https://is.gd/OUu0HF

**Table 2:**
| R[kOhm] | C[uF] | U1 (V) | A. (mA) | U2+ (V) | U2- (V) | U3+ (V) | U3- (V) |
|-------|-------|--------|---------|---------|---------|---------|---------|
| 0.1   | 0     | 20     | 31.8    | 5.0     | 0.0     | 15.0    | -20.0   |
| 0.1   | 1     | 20     | 31.8    | 5.0     | 0.0     | 15.0    | -20.0   |

![oscillogram](Capture%20d%E2%80%99%C3%A9cran%202026-04-21%20195618.png)

![oscillogram](Capture%20d%E2%80%99%C3%A9cran%202026-04-21%20195644.png)

**Characteristics:**
- **Operation:** A full-wave rectifier (often using a diode bridge) converts both halves of the input AC waveform into a pulsing DC output.
- **Forward/Reverse Context:** In a typical bridge setup, two diodes are forward-biased during the positive half-cycle, while the other two are reverse-biased. During the negative half-cycle, the roles switch, but the current through the load still flows in the same direction.
- **Efficiency:** Because both halves of the AC wave are collected, it is twice as efficient as a half-wave rectifier. It delivers a higher average output voltage and is much easier to smooth with a filter capacitor.
