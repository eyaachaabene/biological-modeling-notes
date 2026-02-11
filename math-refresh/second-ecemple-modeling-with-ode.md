# Mixing Problem – Math Refresh Notes

## Problem Data

Tank capacity: 1000 gallons  

Initial state:
- Volume = 800 gallons  
- Pollution = 2 oz  

Let:

q(t) = amount of pollution (oz)

General rule for mixing problems:

dq/dt = rate in − rate out

---

# Phase 1: Before pollution reaches 500 oz

Let t₁ be the time such that:

q(t₁) = 500

### Inflow

- Flow rate = 3 gal/hr  
- Concentration = 5 oz/gal  

Pollution entering:

3 × 5 = 15 oz/hr

### Outflow

- Flow rate = 3 gal/hr  
- Concentration = q(t) / V(t)

Since inflow = outflow:

V(t) = 800  (volume constant)

Pollution leaving:

3 * q / 800

---

### Differential Equation (Phase 1)

dq/dt = 15 − (3/800)q

Initial condition:

q(0) = 2

Linear first-order ODE.

---

# Phase 2: After pollution reaches 500 oz

Now:

Inflow:
- 2 gal/hr
- 0 oz/gal  
→ No pollution enters

Outflow:
- 4 gal/hr
- Concentration = q(t) / V(t)

---

### Volume in Phase 2

Net change:

In = 2  
Out = 4  
→ Volume decreases by 2 gal/hr

So:

V(t) = 800 − 2(t − t₁)

---

### Differential Equation (Phase 2)

dq/dt = − 4q / (800 − 2(t − t₁))

Condition:

q(t₁) = 500

Separable equation.

---

