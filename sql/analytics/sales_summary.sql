SELECT
    COUNT(*) AS total_carts,
    COUNT(DISTINCT user_id) AS total_customers,
    SUM(total) AS gross_revenue,
    SUM(discounted_total) AS net_revenue,
    SUM(total - discounted_total) AS total_discount
FROM carts;