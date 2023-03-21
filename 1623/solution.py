SELECT s.name, MAX(e.score) AS score
FROM student s
JOIN exam e
ON s.id = e.student_id
GROUP BY s.name
ORDER BY score DESC;