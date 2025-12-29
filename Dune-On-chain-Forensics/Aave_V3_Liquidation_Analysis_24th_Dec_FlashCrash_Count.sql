/* Forensic Audit: 24th Dec Flash Crash Liquidation Count
   Objective: Quantify the protocol impact during the -72% CEX price deviation.
*/

SELECT 
    -- We use a Case statement to provide a clear audit status
    count(*) as total_liquidations,
    CASE 
        WHEN count(*) = 0 THEN 'SAFE' 
        ELSE 'ALERT' 
    END as protocol_status
FROM aave_v3_ethereum.Pool_evt_LiquidationCall
WHERE evt_block_time >= CAST('2025-12-24 09:10:00' AS TIMESTAMP)
AND evt_block_time <= CAST('2025-12-24 09:30:00' AS TIMESTAMP)
