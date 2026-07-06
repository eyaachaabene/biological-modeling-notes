# Modeling Viral Spread
**Graw & Perelson (2016)**

## 1. Biological problem
Understanding how viral infection spreads within a host when viruses can transmit by distinct routes (cell-free vs cell-to-cell). The relative importance of these routes in vivo remains unclear for many pathogens.

## 2. Modeling framework
- Reviews mathematical approaches used to disentangle transmission routes: ODE extensions, spatial models, and agent-based models  
- Emphasizes identifiability problems — why viral-load time series alone rarely suffice to tell which route dominates  
- Highlights how single-cell imaging and microfluidic experiments could supply the data models need

Key idea: combine mechanistic model variants with richer, route-aware data to separate cell-free and cell-to-cell contributions.

## 3. Why mathematics mattered
- Organized the model classes needed to represent alternate transmission processes  
- Exposed where data are insufficient for parameter identification and suggested which measurements would help

## 4. Limitations
- Viral-load data alone produce weak identifiability for transmission-route parameters  
- Bridging models and new experimental modalities remains technically and logistically challenging

## 5. My research question
How should I parameterize the cell-to-cell term in my project 02 models so that it remains distinguishable from the cell-free term when using typical viral-load datasets? This review provides the conceptual backbone for project 02.
