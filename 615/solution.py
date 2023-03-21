SELECT d.name AS department, ROUND(AVG(s.salary), 5) AS average_salary, 
CASE 
    WHEN AVG(s.salary) > (SELECT AVG(salary) FROM salary) THEN 'higher' 
    WHEN AVG(s.salary) < (SELECT AVG(salary) FROM salary) THEN 'lower' 
    ELSE 'same' 
END AS compare 
FROM salary s 
JOIN department d ON s.department_id = d.id 
GROUP BY d.name 
ORDER BY d.id;