"""
Aave V3 Insolvency Simulation: Monte Carlo Approach
Simulating protocol risk under 10,000 extreme market volatility scenarios.
"""

import numpy as np
import matplotlib.pyplot as plt

class SolvencySimulator:
    def __init__(self, iterations=10000):
        self.iterations = iterations
        # Parameters derived from Dec 24 Flash Crash event
        self.initial_price = 86600
        self.crash_volatility = 0.72  # Observed -72.15% drop
        self.ltv_threshold = 0.85     # Aave V3 BTC Liquidation Threshold

    def run_simulation(self):
        print(f"[*] Running {self.iterations} Monte Carlo iterations...")
        
        # Generating normally distributed price shocks
        shocks = np.random.normal(loc=-0.05, scale=self.crash_volatility, size=self.iterations)
        
        # Identifying "Insolvent" iterations (where price drop > 15% for an 85% LTV loan)
        insolvency_mask = shocks < -0.15
        insolvency_prob = np.sum(insolvency_mask) / self.iterations
        
        print(f"[!] Simulation Complete.")
        print(f"    Probability of Liquidation Event: {insolvency_prob:.2%}")
        
        return shocks

    def plot_results(self, shocks):
        plt.figure(figsize=(10, 6))
        plt.hist(shocks, bins=100, color='royalblue', alpha=0.7, edgecolor='black')
        plt.axvline(x=-0.15, color='crimson', linestyle='--', label='Liquidation Threshold (LTV 85%)')
        plt.title("Monte Carlo Distribution: Potential Market Shocks")
        plt.xlabel("Price Change Percentage")
        plt.ylabel("Frequency")
        plt.legend()
        plt.show()

if __name__ == "__main__":
    simulator = SolvencySimulator()
    results = simulator.run_simulation()
    # simulator.plot_results(results) # Uncomment to view plot locally
