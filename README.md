# Mathematical Biology — Self-Directed Research Notes

*Self-directed preparation for graduate research in applied mathematics for biological systems, with a long-term goal of pursuing a PhD in this domain.*

## About This Repository

I am a final-year computer engineering student (IGL track, ISIMS, Tunisia) with a background in software engineering, machine learning, optimization, and embedded systems. I created this repository as an independent study to build concrete competency in mathematical and computational biology ahead of formal graduate research. The work here focuses on ODE-based dynamical modeling, viral dynamics, parameter inference, and biological network analysis — these are self-initiated research projects, not coursework. These are working research notes rather than polished papers, but I document every project to the standard of reproducible research.

## Repository Structure

```
biological-modeling-notes/
├── 01-within-host-viral-dynamics/     # TIV model, parameter fitting, sensitivity analysis
├── 02-transmission-mode-comparison/   # Cell-free vs cell-to-cell viral spread (Graw & Perelson 2016)
├── 03-agent-based-infection-spread/   # (in progress)
├── 04-model-selection-and-inference/  # (planned)
├── 05-biological-network-graph-theory/# (planned)
├── math-refresh/                      # Mathematical foundations and worked examples
└── reading-notes/                     # Annotated paper summaries
```

Each numbered project folder contains its own README with the biological question, model description, key results, and references.

## Projects

### 01 — Within-Host Viral Dynamics
**Question:** Can a TIV ODE model reproduce human influenza A viral-load trajectories and which parameters control peak and clearance?  
**Model:** TIV ODE system (Nowak & Bangham 1996), fitted to human influenza A data (Baccam et al. 2006)  
**Methods:** Baseline simulation, R0 computation, sensitivity analysis for delta and p, Nelder–Mead parameter estimation in log-space  
**Key result:** The fitted TIV model reproduced the observed viral-load peak and decay, and sensitivity analysis showed model outputs are most sensitive to infected-cell clearance rate (delta) and viral production rate (p).  
**Folder:** [01-within-host-viral-dynamics](./01-within-host-viral-dynamics/)

### 02 — Transmission Mode Comparison
**Question:** Does the dominant viral transmission route (cell-free vs cell-to-cell) change predicted infection dynamics, and what are the implications for antiviral drug efficacy?  
**Model:** Three ODE variants — cell-free only, cell-to-cell only, combined — based on Graw & Perelson (2016)  
**Methods:** Cross-model comparison of viral load and target cell depletion, beta_c sweep, drug efficacy simulation with route-specific epsilon parameter  
**Key result:** [TO BE FILLED AFTER RUNNING]  
**Folder:** [02-transmission-mode-comparison](./02-transmission-mode-comparison/)

### 03 — Agent-Based Infection Spread *(in progress)*

### 04 — Model Selection and Inference *(planned)*

### 05 — Biological Network Analysis *(planned)*

## Reading Notes

The `reading-notes/` folder contains my annotated summaries of papers I read during this preparation, written as personal study notes rather than formal reviews. Papers covered so far are listed in [reading-notes/](./reading-notes/).

## Mathematical Background

The `math-refresh/` folder contains worked examples and notes on ODE theory, stability analysis, and probability drawn from my engineering mathematics curriculum and extended independently.

## Context and Motivation

My engineering background gives me an advantage most mathematical biology students do not have: I can build end-to-end pipelines from model equations to fitted parameters to deployable code. I demonstrated that in an uncertainty-aware computer vision system for a robotic sorting arm (PFA, international team across Tunisia, Germany hka university , and Oman gutech ) and in a combinatorial route-optimization platform I helped develop. This repository is the bridge I am building between that engineering skill set and graduate-level mathematical biology; I use it to practice modeling rigor, reproducible parameter inference, and clear documentation. I aim to pursue a PhD in applied mathematics for biological systems, and these projects are structured preparation for that work. I find the intellectual challenge of using low-dimensional ODEs and dynamical-systems ideas to capture emergent biological behavior both concrete and tractable.

## Technical Stack

Python, NumPy, SciPy, Matplotlib, Jupyter Notebook

## Contact

Name: Eya Chaabene  
Email: eya.chaabene@ieee.org  
LinkedIn:https://www.linkedin.com/in/eya-chaabene-b33369278/
GitHub: github.com/eyaachaabene
