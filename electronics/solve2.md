# Measurement Report — Direct Current Circuits: Lab No. 1, Part 1

## **SOLVED — Set 2: R_A = 1 kΩ, R_B = 3 kΩ, R_C = 5 kΩ**

**School of Computer Science & Technologies**

| | | |
|---|---|---|
| **Date:** | **Laboratory Subject:** | **Student Name and Surname:** |
| **Teacher:** | Direct current circuits. Equivalent resistance. | |
| **Grade/Points:** | | **Student No.:** |

---

## Aims of Laboratory

- Student will collect measurement data in order to prove Ohm's and the 1st & 2nd Kirchhoff's laws
- Student will be aware of difference between connection in series and parallelly connection of resistors

---

## Scope of Experiments

### 1. Resistors Connected in Series

**Performing measurements and calculations:**

1.1. Chosen resistors: R_A = 1 kΩ, R_B = 3 kΩ, R_C = 5 kΩ

1.2–1.4. Resistance measurements and equivalent resistance recorded in Table 1.1.

1.5–1.7. Circuit connected per Fig. 1.2 with V_PS = 10 V. Current and voltage measurements in Table 1.2.

**Fig. 1.1.** — Series connection for equivalent resistance measurement:
```
    ┌──[R_A]──[R_B]──[R_C]──┐
    │                        │
   (Ω) Multimeter           │
    │                        │
    └────────────────────────┘
```

**Fig. 1.2.** — Series circuit with power supply:
```
     ┌──[R_A]──┬──[R_B]──┬──[R_C]──┐
     │    V_A   │    V_B   │    V_C   │
    (+)        (V)        (V)        (V)
   10V PS       │         │         │
    (-)         │         │         │
     └──(A)────┴─────────┴─────────┘
           I
```

#### Table 1.1. — Series Resistance

| R_A [Ω] | R_B [Ω] | R_C [Ω] | R_Eq measured [Ω] | R_Eq calculated [Ω] |
|----------|----------|----------|--------------------|----------------------|
| 1000     | 3000     | 5000     | 9000               | 1000 + 3000 + 5000 = **9000** |

**Calculation:** R_Eq = R_A + R_B + R_C = 1000 + 3000 + 5000 = **9000 Ω = 9 kΩ**

#### Table 1.2. — Series Circuit Measurements (V_PS = 10 V)

| I [mA] | V_A [V] | V_B [V] | V_C [V] | V_A + V_B + V_C [V] |
|--------|---------|---------|---------|----------------------|
| 1.111  | 1.111   | 3.333   | 5.556   | **10.000**           |

**Calculations:**

- I = V / R_Eq = 10 / 9000 = **1.111 mA**
- V_A = I × R_A = 0.001111 × 1000 = **1.111 V**
- V_B = I × R_B = 0.001111 × 3000 = **3.333 V**
- V_C = I × R_C = 0.001111 × 5000 = **5.556 V**
- **Kirchhoff's Voltage Law (KVL):** V_A + V_B + V_C = 1.111 + 3.333 + 5.556 = **10.000 V = V_PS** ✓

---

### 2. Resistors Connected in Parallel

**Performing measurements and calculations:**

1.1. Same resistors: R_A = 1 kΩ, R_B = 3 kΩ, R_C = 5 kΩ

1.2–1.4. Resistance measurements and equivalent resistance recorded in Table 2.1.

1.5–1.7. Circuit connected per Fig. 2.2 with V_PS = 10 V. Current and voltage measurements in Table 2.2.

**Fig. 2.1.** — Parallel connection for equivalent resistance measurement:
```
    ┌──[R_A]──┐
    ├──[R_B]──┤
    ├──[R_C]──┤
    │         │
   (Ω) Multimeter
    │         │
    └─────────┘
```

**Fig. 2.2.** — Parallel circuit with power supply:
```
         I_total
     ┌───(A)───┬─────────┬─────────┐
     │         │         │         │
    (+)      [R_A]     [R_B]     [R_C]
   10V PS    (A)I_A    (A)I_B    (A)I_C
    (-)        │         │         │
     │         │         │         │
     └─────(V)─┴─────────┴─────────┘
           V = 10V
```

#### Table 2.1. — Parallel Resistance

| R_A [Ω] | R_B [Ω] | R_C [Ω] | R_Eq measured [Ω] | R_Eq calculated [Ω] |
|----------|----------|----------|--------------------|----------------------|
| 1000     | 3000     | 5000     | 652.17             | 1/(1/1000 + 1/3000 + 1/5000) = **652.17** |

**Calculation:**

1/R_Eq = 1/R_A + 1/R_B + 1/R_C = 1/1000 + 1/3000 + 1/5000

1/R_Eq = 15/15000 + 5/15000 + 3/15000 = 23/15000

R_Eq = 15000/23 = **652.17 Ω**

#### Table 2.2. — Parallel Circuit Measurements (V_PS = 10 V)

| V [V] | I_A [mA] | I_B [mA] | I_C [mA] | I_total measured [mA] | I_A + I_B + I_C [mA] |
|-------|----------|----------|----------|-----------------------|------------------------|
| 10.000| 10.000   | 3.333    | 2.000    | 15.333                | **15.333**             |

**Calculations:**

- V = 10 V (same across all parallel resistors)
- I_A = V / R_A = 10 / 1000 = **10.000 mA**
- I_B = V / R_B = 10 / 3000 = **3.333 mA**
- I_C = V / R_C = 10 / 5000 = **2.000 mA**
- **Kirchhoff's Current Law (KCL):** I_A + I_B + I_C = 10.000 + 3.333 + 2.000 = **15.333 mA = I_total** ✓
- **Verification:** I_total = V / R_Eq = 10 / 652.17 = **15.333 mA** ✓
