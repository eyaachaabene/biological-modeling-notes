# A Simple Cellular Automaton Model for Influenza A Viral Infections
**Beauchemin, Samuel & Tuszynski (2005)**

## 1. Biological problem
Assess how spatial structure and local depletion of susceptible cells affect viral spread, since well-mixed ODEs can miss spatial effects that alter infection outcome.

## 2. Modeling framework
- Builds a 2D cellular automaton where each grid site is healthy epithelial, infected, dead, or immune  
- Infection spreads probabilistically to neighboring sites; the model includes rules for regeneration of dead epithelial cells and immune-cell proliferation  
- Validates the CA against clinical influenza A data and investigates sensitivity to initial infected-cell distribution and regeneration/proliferation rules

Key idea: relaxing the well-mixed assumption uncovers spatial mechanisms (local dead zones, clustering) that alter kinetics in ways a homogeneous ODE cannot capture.

## 3. Why mathematics mattered
- Showed that simple spatial rules produce dynamics consistent with uncomplicated influenza A infections  
- Helped identify which mechanistic rules (initial seeding, regeneration, immune proliferation) control infection spread

## 4. Limitations
- The CA is intentionally simple; its conclusions apply best to uncomplicated infections where the modeled rules are appropriate  
- Mapping CA parameters to measurable biological rates requires careful calibration

## 5. My research question
How should I translate the CA rules (infection probability, regeneration, immune proliferation) into the agent-based framework for project 03 so that results remain comparable to my ODE-based benchmarks? This paper provides the methodological template for that work.
