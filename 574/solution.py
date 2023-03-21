SELECT Name
FROM (
    SELECT Name, AVG(Score) AS avg_score
    FROM Student
    WHERE Subject NOT IN ('Math')
    GROUP BY Name
) AS temp
WHERE avg_score = (SELECT MAX(avg_score) FROM (
    SELECT Name, AVG(Score) AS avg_score
    FROM Student
    WHERE Subject NOT IN ('Math')
    GROUP BY Name
) AS temp);