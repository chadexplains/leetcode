SELECT
    year,
    ROUND(
        COUNT(CASE WHEN sender_id != send_to_id THEN 1 END) /
        COUNT(*)
    , 2) AS accept_rate
FROM
    (
    SELECT
        YEAR(request_date) AS year,
        sender_id,
        send_to_id
    FROM
        FriendRequest
    ) AS t1
    JOIN
    (
    SELECT
        YEAR(request_date) AS year,
        COUNT(*) AS total_count
    FROM
        FriendRequest
    GROUP BY
        YEAR(request_date)
    ) AS t2
    ON t1.year = t2.year
GROUP BY
    year;