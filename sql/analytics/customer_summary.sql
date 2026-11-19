SELECT
    user_id,
    COUNT(*) AS total_carts,
    SUM(total) AS gross_revenue,
    SUM(discounted_total) AS net_revenue,
    SUM(total - discounted_total) AS total_discount
FROM carts
GROUP BY user_id
ORDER BY net_revenue DESC;