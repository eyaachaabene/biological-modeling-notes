# Modeling with First Order Differential Equations

## Overview
This document summarizes **first-order differential equation modeling**, with examples from **mixing problems, population growth, and falling objects**.  
It focuses on **how to derive the ODE**, apply assumptions, and implement numerical solutions in Python.

---

## 1. Concept

**Mathematical modeling** translates a real-world dynamic system into an **equation describing how the system evolves over time**.  

### General Form for a First-Order ODE:

\[
\frac{dQ}{dt} = \text{Rate In} - \text{Rate Out}
\]

Where:  
- \(Q(t)\) = quantity of interest at time \(t\)  
- Rate In = input flow (could be constant or time-dependent)  
- Rate Out = output flow (depends on \(Q\) and system properties)

---

## 2. Example: Salt Mixing in a Tank

### Problem
- Tank contains water with initial salt \(Q_0\).  
- Water enters at rate \(F_\text{in}\) with concentration \(C_\text{in}(t)\).  
- Water leaves at rate \(F_\text{out}\) carrying salt proportional to current concentration.  

### Assumptions
- **Well-mixed tank**: salt concentration is uniform throughout.  
- Constant inflow/outflow rates unless specified.  
- No chemical reactions changing salt amount.

### Differential Equation
\[
Q'(t) = F_\text{in} \cdot C_\text{in}(t) - F_\text{out} \cdot \frac{Q(t)}{V(t)}
\]

Where \(V(t)\) is the tank volume:

\[
V(t) = V_0 + (F_\text{in} - F_\text{out}) \cdot t
\]

**Initial condition:**

\[
Q(0) = Q_0
\]

---

