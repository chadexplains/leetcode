SELECT survey
FROM (
    SELECT s1.survey, SUM(s1.action = 'answer') / COUNT(*) AS answer_rate
    FROM survey_log s1
    JOIN survey_log s2
    ON s1.survey = s2.survey
    WHERE s1.action = 'show' AND s2.action = 'answer'
    GROUP BY s1.survey
) AS t
ORDER BY answer_rate DESC
LIMIT 1;