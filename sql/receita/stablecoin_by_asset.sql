SELECT
    month,
    asset,
    SUM(total_value_brl) AS stablecoin_volume_brl,
    SUM(operation_count) AS operation_count
FROM 'data/gold/receita_stablecoin_activity.csv'
WHERE stablecoin_flag = TRUE
GROUP BY
    month,
    asset
ORDER BY
    month,
    asset;
