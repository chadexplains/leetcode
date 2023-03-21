SELECT
    player_id AS Id,
    MAX(score) AS Score
FROM
    Scores
GROUP BY
    player_id;