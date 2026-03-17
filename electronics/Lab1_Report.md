# Measurement Report — Direct Current Circuits: Lab No. 1, Part 1

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

1.1. Choose 3 resistors on laboratory PCB: R_A, R_B, R_C (except R6, R9, R12).

1.2. Perform measurements of resistance of chosen components, results place into relevant cells in Table 1.1.

1.3. Connect circuit according to schematic diagram given on Fig. 1.1.

1.4. Read value of R_Eq displayed on the multi meter and write down into Table 1.1.

1.5. Connect circuit according to schematic diagram given on Fig. 1.2. — use the same resistors.

1.6. Attune value of 10 Volts on the Power Supply (using right knob on the front panel); pay attention not to exceed value of current above 20 mA.

1.7. Perform measurements of current and voltages. Results put into Table 1.2.

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
|          |          |          |                    | R_A + R_B + R_C      |

#### Table 1.2. — Series Circuit Measurements (V_PS = 10 V)

| I [mA] | V_A [V] | V_B [V] | V_C [V] | V_A + V_B + V_C [V] |
|--------|---------|---------|---------|----------------------|
|        |         |         |         |                      |

---

### 2. Resistors Connected in Parallel

**Performing measurements and calculations:**

1.1. Choose the same 3 resistors on laboratory PCB: R_A, R_B, R_C (except R6, R9, R12).

1.2. Perform measurements of resistance of chosen components, results place into relevant cells in Table 2.1.

1.3. Connect circuit according to schematic diagram given on Fig. 2.1.

1.4. Read value of R_Eq displayed on the multi meter and write down into Table 2.1.

1.5. Connect circuit according to schematic diagram given on Fig. 2.2. — use the same resistors.

1.6. Attune value of 10 Volts on the Power Supply (using right knob on the front panel); pay attention not to exceed value of current above 20 mA.

1.7. Perform measurements of current and voltages. Results place into relevant cells in Table 2.2.

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
|          |          |          |                    | 1/(1/R_A + 1/R_B + 1/R_C) |

#### Table 2.2. — Parallel Circuit Measurements (V_PS = 10 V)

| V [V] | I_A [mA] | I_B [mA] | I_C [mA] | I_total [mA] | I_A + I_B + I_C [mA] |
|-------|----------|----------|----------|---------------|------------------------|
|       |          |          |          |               |                        |
