SELECT customer_id
FROM customer
JOIN orders ON customer.customer_id = orders.customer_id
GROUP BY customer.customer_id
HAVING COUNT(DISTINCT orders.product_key) = (SELECT COUNT(DISTINCT product_key) FROM product);