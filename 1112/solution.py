SELECT s.name, e.subject, e.score
FROM student s
JOIN exam e ON s.id = e.student
WHERE (e.student, e.score) IN (
    SELECT student, MAX(score)
    FROM exam
    GROUP BY student
)
ORDER BY s.name, e.subject;