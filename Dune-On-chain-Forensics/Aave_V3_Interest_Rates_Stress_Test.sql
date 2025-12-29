/* Query 2: Interest Rate Spikes during Flash Crash (UTC Time) */
SELECT 
    block_hour AS time,
    deposit_rate AS deposit_apy,
    variable_borrow_rate AS borrow_apy
FROM aave.interest_rates
WHERE symbol = 'WBTC'
AND blockchain = 'ethereum' -- etheruem: 'block_hour' not 'hour'
AND block_hour >= CAST('2025-12-24 08:00:00' AS TIMESTAMP)
AND block_hour <= CAST('2025-12-24 12:00:00' AS TIMESTAMP) -- UTC 08:00 到 12:00 (對應香港時間 16:00 到 20:00)
ORDER BY 1 DESC
