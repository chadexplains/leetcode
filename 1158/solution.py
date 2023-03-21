SELECT seller_id, MIN(order_date) AS first_order FROM
    (SELECT o.user_id, o.order_date, p.seller_id
     FROM Orders o
     JOIN Products p ON o.product_id = p.product_id) AS t
GROUP BY seller_id
HAVING COUNT(*) > 1;