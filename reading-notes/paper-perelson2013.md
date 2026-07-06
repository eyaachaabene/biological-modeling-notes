# Modeling the Within-Host Dynamics of HIV Infection
**Perelson & Ribeiro (2013)**

## 1. Biological problem
Trace the quantitative within-host dynamics of HIV: acute infection dynamics, response to therapy, and generation of escape variants.

## 2. Modeling framework
- Starts from the TIV equations I implemented in project 01 and then extends them progressively  
- Adds drug efficacy as an epsilon factor reducing the infection term (the same formalism I use in project 02 drug simulations)  
- Describes multi-phase viral decay under therapy and models of latent reservoirs and long-lived infected cells  
- Diagram: uninfected cells → infected cells → productively infected, long-lived infected, or latently infected; latently infected cells can proliferate and sustain the reservoir

Key idea: incremental model extensions map directly to distinct biological processes (drug action, latency, reservoir maintenance).

## 3. Why mathematics mattered
- Yielded quantitative estimates for production, clearance, and decay phases in HIV infection  
- Made it possible to interpret therapy responses and to quantify rates of appearance of escape variants

## 4. Limitations
- Latent reservoirs and cell-to-cell transmission remain hard to parameterize from routine clinical data  
- Some clinically important processes require experimental data types beyond standard viral-load measurements

## 5. My research question
Which elements of the TIV extensions (epsilon, long-lived compartments, latent proliferation) are most critical when I move from influenza data in project 01 to drug-simulation experiments in project 02? The paper links my project 01 implementation to the drug and transmission work in project 02.
