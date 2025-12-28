"""
Aave V3 Stress Test: Simulating Oracle Failure during Dec 24 Flash Crash
This script quantifies the theoretical risk if the protocol had adopted the Binance BTC/USD1 wick price.
"""

import pandas as pd

# 1. Input parameters directly from the Dec 24 Flash Crash
NORMAL_MARKET_PRICE = 86608.68  # MA(7) price at 17:19
FLASH_CRASH_PRICE = 24111.22   # The extreme wick low
PRICE_DROP_PCT = (FLASH_CRASH_PRICE - NORMAL_MARKET_PRICE) / NORMAL_MARKET_PRICE

print(f"--- Dec 24 Market Shock Summary ---")
print(f"Localized Price Drop: {PRICE_DROP_PCT:.2%}\n") # Results in -72.15%

# 2. Stress Test Simulation Logic
def run_stress_test(collateral_usd, debt_usd, liquidation_threshold=0.85):
    """
    Simulates the impact on a loan's Health Factor (HF).
    """
    # Standard HF calculation
    current_hf = (collateral_usd * liquidation_threshold) / debt_usd
    
    # HF if the Oracle failed and used the flash crash price
    crash_collateral_value = collateral_usd * (1 + PRICE_DROP_PCT)
    crash_hf = (crash_collateral_value * liquidation_threshold) / debt_usd
    
    print(f"Position Scenario: ${collateral_usd/1e6}M Collateral / ${debt_usd/1e6}M Debt")
    print(f"- Normal Health Factor: {current_hf:.2f}")
    print(f"- Crash Health Factor: {crash_hf:.2f}")
    
    if crash_hf < 1.0:
        print(">>> STATUS: LIQUIDATION TRIGGERED. Potential for Bad Debt.")
    else:
        print(">>> STATUS: POSITION SAFE.")

# 3. Running simulations for different Risk Profiles
print("--- Stress Test Results ---")
run_stress_test(collateral_usd=1000000, debt_usd=800000) # Aggressive borrower
print("-" * 30)
run_stress_test(collateral_usd=1000000, debt_usd=500000) # Conservative borrower
