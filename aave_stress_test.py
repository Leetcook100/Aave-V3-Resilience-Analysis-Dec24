import ccxt
import pandas as pd
from datetime import datetime

# --- PART 1: Data Acquisition & Anomaly Detection ---
def get_crash_params():
    exchange = ccxt.binance()
    # 12/24 Start Time in UTC
    since = int(datetime(2025, 12, 24, 0, 0).timestamp() * 1000)
    
    print("Scanning Binance for flash crash anomalies...")
    ohlcv = exchange.fetch_ohlcv('BTC/USD1', timeframe='1m', since=since, limit=1440)
    df = pd.DataFrame(ohlcv, columns=['ts', 'open', 'high', 'low', 'close', 'vol'])
    
    # Identify the exact second of the -72% drop
    crash_row = df.loc[(df['low'] - df['open']) / df['open'] < -0.5].iloc[0]
    
    return crash_row['open'], crash_row['low']

# --- PART 2: Stress Test Logic (Your Original Code) ---
def run_stress_test(market_p, crash_p, collateral_usd=1000000, debt_usd=800000):
    drop_pct = (crash_p - market_p) / market_p
    liquidation_threshold = 0.85
    
    # Calculate HF if Oracle adopted crash price
    crash_hf = (collateral_usd * (1 + drop_pct) * liquidation_threshold) / debt_usd
    
    print(f"\n--- Stress Test for ${collateral_usd/1e6}M Position ---")
    print(f"Detected Drop: {drop_pct:.2%} (from ${market_p:,.2} to ${crash_p:,.2})")
    print(f"Resulting Health Factor: {crash_hf:.2f}")
    
    if crash_hf < 1.0:
        print(">>> STATUS: LIQUIDATION TRIGGERED.")

# --- PART 3: Execution ---
m_price, c_price = get_crash_params()
run_stress_test(m_price, c_price)
