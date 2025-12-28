import pandas as pd

# Data directly from the Dec 24 Binance Flash Crash observation
normal_price = 86608.68  # MA(7) price before the crash
crash_price = 24111.22   # The extreme wick price
price_drop_pct = (crash_price - normal_price) / normal_price

print(f"--- 12/24 Flash Crash Parameters ---")
print(f"Observed Price Drop: {price_drop_pct:.2%}")

# Stress Test: Impact on a standard Aave loan
def simulate_position_liquidation(collateral_usd, debt_usd, threshold=0.85):
    # Calculate current Health Factor
    current_hf = (collateral_usd * threshold) / debt_usd
    
    # Calculate Health Factor if Oracle adopted the crash price
    crash_collateral_value = collateral_usd * (1 + price_drop_pct)
    crash_hf = (crash_collateral_value * threshold) / debt_usd
    
    print(f"\nSimulation for a ${collateral_usd/1e6}M Position:")
    print(f"- Normal Health Factor: {current_hf:.2f}")
    print(f"- Crash Health Factor: {crash_hf:.2f}")
    
    if crash_hf < 1.0:
        print("Result: POSITION LIQUIDATED. Potential Bad Debt if liquidity is thin.")
    else:
        print("Result: POSITION SAFE.")

# Run simulation for a typical whale position
simulate_position_liquidation(collateral_usd=100000000, debt_usd=75000000)
