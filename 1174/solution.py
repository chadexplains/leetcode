SELECT
    customer_id,
    AVG(wait_time) AS average_waiting
FROM
    (
    SELECT
        o.customer_id,
        (d.order_date - o.order_date) AS wait_time
    FROM
        delivery d
        JOIN orders o ON d.customer_id = o.customer_id
        AND d.order_date >= o.order_date
    ) t
GROUP BY
    customer_id;