# NRFE: Normalized Ricci Flow with Entropy Optimization

## 📌 Overview

This repository provides a reproducible implementation of the **NRFE (Normalized Ricci Flow with Entropy Optimization)** method for community detection in complex networks.

The method integrates:
- Ollivier-Ricci curvature
- Ricci flow-based edge reweighting
- Entropy-based optimization
- Community refinement strategies

It is designed to improve the accuracy and robustness of community detection across different network structures.

---

## 📁 Project Structure

NRFE/
│
├── data/
│ └── (optional datasets)
│
├── src/
│ ├── curvature.py # Ricci curvature computation
│ ├── ricci_flow.py # Ricci flow process
│ ├── entropy.py # Entropy calculation
 
│
├── experiments/
│ └── run_karate.py # Example experiment
│
├── requirements.txt
├── README.md
---

## ⚙️ Installation

We recommend using Python 3.8+.

```bash
pip install -r requirements.txt

🔁 Reproducibility

To reproduce the results:

Load or prepare the network
Run Ricci flow to update edge weights
Perform edge pruning
Apply community repair
Extract connected components as communities
Evaluate results

⚙️ Parameters
Parameter	Description
T	Number of iterations
tau	Edge pruning interval
theta	Fraction of removed edges
step_size	Learning rate
🧠 Method Summary
Initialize edge weights
Compute Ricci curvature
Update weights via Ricci flow
Remove edges periodically
Repair small communities
Compute final partition
⚠️ Notes
Computational cost may increase for large networks
Parameter tuning can affect performance
Designed for undirected graphs



