# Aave-V3-Resilience-Analysis-Dec24
Investigating Aave V3's resilience during the 12/24 BTC flash crash (-70%) using Dune SQL, Python VaR modeling, and stress testing.


## 🐍 Project 2: Stress Testing & Solvency Simulation (Python)
**Goal:** Quantify the protocol's theoretical exposure to the Dec 24 extreme volatility event.

- **The Shock Scenario:** On Dec 24, BTC/USD1 experienced a localized crash of **-72.15%** within seconds.
- **Simulated Oracle Failure:** Developed a stress-testing script to simulate the impact on Aave V3's TVL if the Oracle had adopted this -72% price deviation instead of the global market price.
- **Key Metrics:** - **Health Factor Impact:** Analyzed how a 72% drop would force overcollateralized positions into immediate liquidation.
    - **Bad Debt Simulation:** Estimated potential protocol insolvency if liquidation depth (liquidity) was insufficient to cover the seized collateral.
