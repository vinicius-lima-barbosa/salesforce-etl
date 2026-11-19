SELECT
    product_id,
    title,
    SUM(quantity) AS total_quantity_sold,
    SUM(total) AS gross_revenue,
    SUM(discounted_total) AS net_revenue
FROM cart_products
GROUP BY product_id, title
ORDER BY net_revenue DESC
LIMIT 10;