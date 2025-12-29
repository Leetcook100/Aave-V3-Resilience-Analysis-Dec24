/* Query 1: Oracle Price Tracking vs Market Flash Crash */
SELECT 
    minute AS time,
    price AS oracle_btc_price
FROM prices.usd
WHERE blockchain = 'ethereum'
AND symbol = 'WBTC'  -- Using WBTC as the proxy for BTC Oracle price on Ethereum
/* 時間換算：香港時間 16:00 到 19:00 = UTC 08:00 到 11:00 */
AND minute >= CAST('2025-12-24 08:00:00' AS TIMESTAMP)
AND minute <= CAST('2025-12-24 11:00:00' AS TIMESTAMP)
ORDER BY 1 ASC

