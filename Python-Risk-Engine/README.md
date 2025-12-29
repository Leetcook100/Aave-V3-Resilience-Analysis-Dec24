# 🛡️ Python Risk Engine

This module provides a quantitative framework to simulate Aave V3's resilience against extreme market volatility.

### 📊 Monte Carlo Simulation Result
By integrating Binance real-time crash data, this engine simulates 10,000 price scenarios to evaluate insolvency risks.

![Risk Distribution](./monte_carlo_solvency.png)

**Key Metrics:**
* **Crash Amplitude:** -72.15% (Modeled from 12/24 Binance Flash Crash)
* **Theoretical Insolvency Probability:** 44.25%
* **Conclusion:** The simulation highlights the vital role of Aave's Oracle price filtering in preventing mass liquidations during high-frequency volatility spikes.

### 📂 Analysis Walkthrough
For a detailed step-by-step technical analysis and code execution, please refer to the [Jupyter Notebook](./Aave_Solvency_Analysis-checkpoint.ipynb).
