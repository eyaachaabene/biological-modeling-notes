## Biological Question
I investigate whether infections driven by direct cell-to-cell transmission produce qualitatively different within-host dynamics than cell-free transmission, and what that implies for invasion thresholds and drug efficacy. I motivate this with examples where cell-to-cell spread is known or suspected to be important (HIV, HCV) and frame the question in terms of how the infection term (T*V vs T*I) changes the model behavior.

## The Three Model Variants
Variant 1 (Cell-free only): the standard TIV model where infection is mediated by free virus (T*V). Variant 2 (Cell-to-cell only): infection scales with contacts between infected and target cells (T*I), leaving V as an observable but not the driver of transmission. Variant 3 (Combined): both routes act simultaneously and can be compared to estimate the relative contribution of each.

## What I Did
I implemented three ODE variants in `src/extended_tiv_model.py`, computed route-specific R0 expressions, and ran a set of simulations: baseline comparison, a sweep of cell-to-cell strength, and simplified drug efficacy experiments that reduce production or cell-free infectivity. Figures illustrate viral load, target-cell depletion, and sensitivity to beta_c.

## Key Results
Under baseline parameters the cell-free reproduction number is approximately R0_cf = 28.308, the cell-to-cell reproduction number is R0_cc = 10.000, and the combined R0 ≈ 38.308.
Project 01 parameter fitting produced: beta ≈ 5.850717384015399e-08, delta ≈ 3.7767607996294075 day⁻¹, p ≈ 334.8481805086686 TCID50/cell/day, and c ≈ 652.3441872921757 day⁻¹; these values are broadly similar in order of magnitude to those reported by Baccam et al. (2006).
Sensitivity analysis indicated that the infected-cell death rate (delta) most strongly controlled infection duration: increasing delta substantially shortens the time the model predicts detectable virus.

## Connection to Project 01
I extended the TIV model from project 01 by introducing a second infection route. The `src/extended_tiv_model.py` module includes the original cell-free model as Variant 1, so the two projects are mathematically consistent and parameter values are shared where applicable.

## References
Graw F, Perelson AS (2016). Modeling viral spread. Annual Review of Virology 3:555–572.

Nowak MA, Bangham CRM (1996). Population dynamics of immune responses to persistent viruses. Science 272:74–79.

Baccam P, Beauchemin C, Macken CA, Hayden FG, Perelson AS (2006). Kinetics of influenza A virus infection in humans. Journal of Virology 80:7590–7599.

Gabel A, Szczurek E, Rateitschak K, Wolkenhauer O, Graw F (2019). FAMoS: A flexible algorithm for model selection. PLOS Computational Biology 15:e1007230.

## How to Run
pip install -r requirements.txt

jupyter notebook notebooks/transmission_mode_comparison.ipynb
