SELECT s.name, g.city
FROM student s
JOIN (
    SELECT student_id, city, MIN(ABS(s.latitude - g.latitude) + ABS(s.longitude - g.longitude)) AS distance
    FROM student s
    CROSS JOIN geography g
    GROUP BY student_id
) t
ON s.id = t.student_id
JOIN geography g
ON t.city = g.city
AND t.distance = ABS(s.latitude - g.latitude) + ABS(s.longitude - g.longitude)
ORDER BY s.name;