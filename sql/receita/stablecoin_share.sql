WITH monthly_totals AS (
    SELECT 
        month,
        SUM(total_value_brl) FILTER (WHERE stablecoin_flag) AS total_stablecoin_brl
    FROM 'data/gold/receita_stablecoin_activity.csv'
    GROUP BY month
),
asset_totals AS (
    SELECT 
        month,
        asset,
        SUM(total_value_brl) AS asset_value_brl
    FROM 'data/gold/receita_stablecoin_activity.csv'
    WHERE stablecoin_flag
    GROUP BY month, asset
)
SELECT 
    a.month,
    a.asset,
    a.asset_value_brl,
    m.total_stablecoin_brl,
    ROUND((a.asset_value_brl / m.total_stablecoin_brl) * 100, 2) AS share_percentage
FROM asset_totals a
JOIN monthly_totals m USING (month)
ORDER BY a.month ASC, a.asset_value_brl DESC
