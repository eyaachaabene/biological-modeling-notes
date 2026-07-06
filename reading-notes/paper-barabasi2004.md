# Network Biology: Understanding the Cell's Functional Organization
**Barabási & Oltvai (2004)**

## 1. Biological problem
Systematically catalogue molecular interactions in the cell and understand how network structure constrains cellular function.

## 2. Modeling framework
- Frames protein interaction, metabolic, and regulatory systems as graphs and studies their degree distributions  
- Introduces the scale-free model where degree distribution follows a power law P(k) ~ k^−γ and a few hub nodes dominate connectivity  
- Connects topology to function: hubs tend to be essential, while peripheral nodes have smaller phenotypic effects

Key idea: network topology (power-law degree distributions and hub structure) provides predictive insight into gene essentiality and system robustness.

## 3. Why mathematics mattered
- Translated large interaction datasets into simple, testable hypotheses about robustness and essentiality  
- Made it possible to prioritize nodes (hubs) for functional follow-up and to reason about network-level consequences of perturbations

## 4. Limitations
- Real biological networks can deviate from idealized scale-free models; degree distributions and inferred hub importance depend on dataset quality and coverage

## 5. My research question
Which centrality measures and community-detection algorithms best reproduce the hub–essentiality relationship on the interaction datasets I plan to analyze in project 05? This review forms the conceptual foundation for the centrality and community analyses I will run.
