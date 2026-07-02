## Biological Question
I studied how influenza A virus spreads inside a single human host by connecting a simple target-cell-limited infection model with a clinical viral-load time course. The central question is whether the observed rise and fall of virus can be explained by a small set of biologically meaningful rates rather than by a more complex immune response model. I wanted a notebook that would make this logic visible, from the equations to the fitting procedure.

## The Model
I implemented the classic Target-Infected-Virus (TIV) model from Nowak and Bangham (1996) and used the parameterization described by Baccam and colleagues (2006) for influenza A infection. The model tracks uninfected target cells, infected cells, and free virus as a coupled system of ordinary differential equations. Its main assumption is that infection is well mixed within the host and that the virus dynamics are driven by target-cell depletion and viral clearance rather than by an explicit immune-cell compartment.

## What I Did
I built a reproducible analysis pipeline with a Python module for the ODE system, a simulation notebook for exploring the baseline dynamics and parameter sensitivity, and a fitting notebook for estimating parameters from digitized patient data. I worked in log-space for viral load because the data span several orders of magnitude and log-scale fitting gives a more balanced view of the trajectory. The notebooks are written as a student’s research record, with the biology stated explicitly at each step.

## Key Results
Under the baseline parameterization, the analytic reproduction number was $R_0 \approx 1.2$, indicating that one infected cell could sustain growth before it died. The least-squares fit returned $\beta \approx 5.85 \times 10^{-8}$, $\delta \approx 3.77$, $p \approx 3.41 \times 10^{2}$, and $c \approx 6.64 \times 10^{2}$, which are broadly in the same range as the values reported by Baccam et al. (2006) despite the simplified single-patient data set. The sensitivity analysis showed that increasing $\delta$ shortened the infection window and reduced peak viral load, making infected-cell clearance the most direct control of infection duration in this model. 

## References
Nowak MA, Bangham CRM (1996). Population dynamics of immune responses to persistent viruses. Science 272:74–79.

Baccam P, Beauchemin C, Macken CA, Hayden FG, Perelson AS (2006). Kinetics of influenza A virus infection in humans. Journal of Virology 80:7590–7599.

## How to Run
pip install -r requirements.txt

jupyter notebook notebooks/01_TIV_model_simulation.ipynb
