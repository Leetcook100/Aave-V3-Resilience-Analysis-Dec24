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



、
### 📉 Market Liquidity & Execution Slippage Analysis
To evaluate the protocol's secondary defense layer, I modeled the market impact of large-scale liquidations using real-time L2 Order Book data.

![Liquidity Depth Curve](liquidity_depth_curve.png)

Key Findings:
Liquidity Threshold: The BTC/USDT market depth on Binance can safely absorb up to approximately 60 BTC in single-block liquidations with minimal slippage.

Catastrophic Slippage: Beyond the 80 BTC threshold, the order book becomes exceptionally thin, with price impact skyrocketing to 100%.

Systemic Risk Conclusion: This "vertical" slippage curve justifies why Aave's decision to ignore the -72% Binance spike was essential. Triggering liquidations into this "liquidity vacuum" would have resulted in massive Bad Debt for the protocol, as collateral could not have been liquidated at any reasonable price.
