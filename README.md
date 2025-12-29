# Aave V3 Resilience Analysis: The Dec 24 Flash Crash Case Study

Investigating Aave V3's systemic stability during the 12/24 BTC flash crash (-72.15%) using multi-stage data pipelines including Dune SQL, Python Risk Modeling, and Stress Testing.

---

## 🚀 Executive Summary
This project evaluates the risk management efficiency of Aave V3. On Dec 24, 2024, a localized flash crash on Binance saw BTC/USD1 drop to **$24,111** in seconds. This study analyzes why Aave remained solvent and quantifies the "What-if" risks if Oracle protections had failed.

## 📂 Project Structure & Modules

### 🔍 [Module 1: Dune On-chain Forensics](https://dune.com/workspace/u/kelvinwong/library/folders/Dune%20On-chain%20Forensics)
- **Goal:** Empirical verification of protocol events during the crash window.
- **Key Tech:** Dune SQL (V2 Engine), Event Log Auditing.
- **Finding:** Confirmed **0 liquidations** on-chain, proving Oracle filter success.

### 🐍 [Module 2: Python Risk Engine](https://github.com/Leetcook100/Aave-V3-Resilience-Analysis-Dec24)
- **Goal:** Quantitative stress testing and counterfactual simulation.
- **Key Tech:** Python (Pandas, CCXT), Anomaly Detection, Monte Carlo.
- **Finding:** Simulated **Bad Debt** accumulation and Health Factor (HF) collapse under simulated Oracle failure.

### 📄 [Module 3: Research Whitepaper](./Research-Reports/)
- **Goal:** Institutional-grade reporting on DeFi security parameters.
- **Key Tech:** Quantitative Analysis, Statistical Risk Modeling (VaR).

---

## 🛠️ Quick Start & Reproducibility
1. **Clone the Repo:** `git clone https://github.com/Leetcook100/Aave-V3-Resilience-Analysis-Dec24.git`
2. **Install Dependencies:** `pip install -r requirements.txt`
3. **Run Stress Test:** `python Python-Risk-Engine/aave_stress_test.py`

## 🔗 External Links
- **Interactive Dashboard:** [View on Dune Analytics](https://dune.com/kelvinwong/dune-on-chain-forensics)
