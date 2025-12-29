import numpy as np
import matplotlib.pyplot as plt
# Import the engine from your other script
from aave_stress_test import AaveRiskEngine 

class SolvencySimulator:
    def __init__(self, iterations=10000):
        self.iterations = iterations
        self.engine = AaveRiskEngine() # Initialize the Binance-connected engine
        
    def get_live_parameters(self):
        """Fetches dynamic parameters from Binance via the Risk Engine."""
        print("[*] Fetching crash volatility parameters from Binance...")
        market_p, crash_p = self.engine.fetch_crash_data()
        
        # Calculate the actual drop observed on Binance during the crash
        real_crash_impact = (crash_p - market_p) / market_p
        
        # Dynamically set initial price and use the absolute crash impact as volatility
        return market_p, abs(real_crash_impact)

    def run_simulation(self):
        # Dynamically fetch values instead of hardcoding
        initial_price, crash_vol = self.get_live_parameters()
        
        print(f"[*] Simulating based on Binance crash volatility: {crash_vol:.2%}")
        shocks = np.random.normal(loc=-0.05, scale=crash_vol, size=self.iterations)
        
        # Logic remains same but data is now 'Live'
        insolvency_mask = shocks < -0.15
        print(f"[!] Probability of Liquidation Event: {np.sum(insolvency_mask)/self.iterations:.2%}")
        return shocks


if __name__ == "__main__":
    # 1. Initialize the simulator
    simulator = SolvencySimulator()
    
    # 2. Run simulation (This automatically triggers aave_stress_test to fetch Binance data)
    results = simulator.run_simulation()
    
    # 3. UNCOMMENT THIS LINE TO SHOW THE PLOT (本地執行必須取消這行的註釋)
    #simulator.plot_results(results)
