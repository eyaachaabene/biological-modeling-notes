# Mathematical and Computational Modeling in Complex Biological Systems

This repository contains notes based on the review article:

**Ji Z., Yan K., Li W., Hu H., Zhu X.**  
*Mathematical and Computational Modeling in Complex Biological Systems*  
BioMed Research International, 2017  

Paper link:  
https://doi.org/10.1155/2017/5958321  

The goal is to summarize classical systemic modeling approaches used in systems biology, especially for complex diseases like cancer.

---

## 1. ODE-based modeling

Ordinary Differential Equation (ODE) models describe how biological variables (e.g. protein concentrations) change continuously over time.

Common functions:
- **Hill function**: models activation or inhibition of proteins
- **Michaelis–Menten kinetics**: models enzyme-catalyzed signaling reactions

Main issue:  
ODE models require many parameters that are often unknown or hard to measure.

Typical solutions:
- Genetic Algorithms  
- Particle Swarm Optimization (often performs better)  
- Scatter Search  
- Stochastic Ranking Evolution Strategy

These approaches are widely used to model intracellular and intercellular signaling in complex diseases.

---

## 2. Petri net-based modeling approaches

Petri nets are graphical and mathematical modeling tools applicable to many systems.

A Petri net is defined by a 5-tuple:  
(P, T, F, W, M0)

They are commonly used to represent signaling pathway networks, especially when concurrency and discrete events are important.

---

## 3. Boolean modeling approaches

In Boolean models, each node has a binary state (0 or 1).  
The future state of a node depends on the current states of its parent nodes through a Boolean function.

Boolean dynamic modeling generally follows three steps:
1. Reconstructing the network  
2. Identifying Boolean functions from the network topology  
3. Analyzing system dynamics with or without perturbations

Advantages:
- Parameter-free
- Efficient for large-scale networks

Example application:
Combining gene set enrichment analysis with Boolean modeling to study signaling changes in dendritic cells infected by influenza virus.

---

## 4. Linear programming approaches

Linear Programming (LP) methods have been applied to:
- Gene regulatory network reconstruction
- Metabolic network analysis
- Cell-specific signaling network inference

These approaches are useful for large systems where constraints can be expressed in linear form.

---

## 5. Agent-based modeling of biological systems

Agent-based models simulate individual entities (cells, molecules) and their interactions.

They can be implemented in:
- 2D models
- 3D models

3D models are often used to mimic tumor tissue dynamics and interactions between tumor cells, stromal cells, and immune cells in heterogeneous microenvironments.

---

## 6. Integrating genetic variation to infer cancer networks

This approach incorporates genetic variation into systemic modeling of intracellular pathways.

It helps explain heterogeneity in cancer networks and supports more personalized interpretations of signaling behavior.

---

## Notes

These are study notes, not a full reproduction of the paper.  
The focus is on understanding the modeling frameworks and when they are used, rather than implementation details.
