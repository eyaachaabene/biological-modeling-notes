# Insect Population Model – Math Refresh Notes

## Problem Statement

A population of insects grows at a rate proportional to its current population.

- In the absence of outside factors, the population triples in 14 days.
- Each day:
  - 15 insects migrate into the region.
  - 16 insects are eaten.
  - 7 insects die naturally.
- Initial population: 100 insects.

Question:
Will the population survive? If not, when does it die out?

---

# 1. Natural Growth (No External Factors)

Let:

P(t) = population of insects

Without migration or deaths:

dP/dt = rP

Solution of this differential equation:

P(t) = P(0)e^{rt}

We are told:

P(14) = 3P(0)

So:

3P(0) = P(0)e^{14r}

3 = e^{14r}

Taking the natural logarithm:

r = ln(3)/14

---

# 2. Model With External Factors

Entries:
- Births = rP
- Migration = +15

Exits:
- 16 eaten
- 7 natural deaths

Total losses = 23

So the full model becomes:

dP/dt = rP + 15 − 23

dP/dt = rP − 8

where:

r = ln(3)/14

Initial condition:

P(0) = 100

---

# 3. Equilibrium Analysis (Survival Condition)

To check long-term behavior, we find equilibrium:

rP − 8 = 0

P* = 8 / r

Since:

r = ln(3)/14 ≈ 0.0785

Then:

P* ≈ 8 / 0.0785 ≈ 102

---

# 4. Interpretation

Initial population = 100  
Equilibrium ≈ 102  

Since 100 < 102:

dP/dt < 0 at t = 0

The population initially decreases.

If it keeps decreasing, the birth term rP becomes smaller, which may lead the population toward extinction.

This model shows a critical threshold:

- If P(0) > 8/r → population grows
- If P(0) < 8/r → population declines toward zero

Here, the system is very close to the threshold, which makes it an interesting borderline case.
