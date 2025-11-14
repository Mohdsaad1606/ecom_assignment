SELECT 
    c.customer_id,
    c.name AS customer_name,
    SUM(oi.quantity * p.price) AS total_spent,
    COUNT(DISTINCT o.order_id) AS total_orders,
    AVG(r.rating) AS avg_rating_given
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
LEFT JOIN reviews r ON p.product_id = r.product_id
GROUP BY c.customer_id, c.name
ORDER BY total_spent DESC
LIMIT 5;
