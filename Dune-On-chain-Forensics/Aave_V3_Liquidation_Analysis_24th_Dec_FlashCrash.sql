
/* SQL脚本和取证说明 */


/* Project: Aave V3 Liquidity Resilience Analysis
   Description: Fetching liquidation events on Aave V3 during the BTC/USD1 flash crash on Binance.
   Event Date: 2025-12-24
*/

SELECT 
    evt_block_time,                            -- Exact timestamp of the liquidation event
    liquidator,                                -- Address of the liquidator (bot or user)
    user AS borrower,                          -- Address of the liquidated user
    debtAsset,                                 -- The asset being repaid to cover the debt
    collateralAsset,                           -- The collateral asset seized by the liquidator
    
    /* Note: Dividing by 1e18 assumes WETH/USDC decimals for demo. 
       In a production dashboard, use 'prices.usd' to get exact USD values. */
    debtToCover / 1e18 AS debt_amount_raw,     
    liquidatedCollateralAmount / 1e18 AS collateral_amount_raw,
    
    evt_tx_hash                                -- Transaction Hash for Etherscan verification
FROM aave_v3_ethereum.Pool_evt_LiquidationCall
WHERE evt_block_time >= CAST('2025-12-24 09:10:00' AS TIMESTAMP) -- UTC 09:10 = HKT 17:10
AND evt_block_time <= CAST('2025-12-24 09:30:00' AS TIMESTAMP)   -- UTC 09:30 = HKT 17:30 -- Focus on the 10-min window around the crash
ORDER BY evt_block_time ASC;
