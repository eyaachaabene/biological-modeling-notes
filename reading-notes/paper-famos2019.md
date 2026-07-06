# FAMoS: A Flexible and Dynamic Algorithm for Model Selection
**Gabel, Hohl, Imle, Fackler & Graw (2019)**

## 1. Biological problem
Choosing an appropriate dynamical model when the system admits many plausible mechanistic descriptions and data are limited.

## 2. Modeling framework
- Introduces FAMoS, an algorithm that searches large model spaces dynamically for candidate dynamical-system structures  
- Uses a mixture of local and non-local search strategies to avoid settling in local minima of the model-space landscape  
- Validates on simulated data and applies the method to experimental data on HIV cell-to-cell transmission

Key idea: treat model selection as an adaptive search problem that balances local refinement with structural moves to explore alternative mechanisms.

## 3. Why mathematics mattered
- Provides a systematic, reproducible way to choose models from many competing hypotheses  
- Demonstrates that algorithmic model selection can recover mechanistic features relevant to cell-to-cell transmission

## 4. Limitations
- Performance depends on the search heuristics and the model-space encoding  
- Validation requires both realistic simulated data and suitable experimental datasets

## 5. My research question
Can I integrate a FAMoS-style selection step into the model-selection cell I added to project 01 to test alternative TIV variants and transmission hypotheses? This paper motivated that cell directly.
