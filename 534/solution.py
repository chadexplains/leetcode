SELECT login_date, COUNT(DISTINCT player_id) AS player_count FROM Logs GROUP BY login_date;