SELECT e.name
FROM Employee e
JOIN Department d ON e.department_id = d.id
WHERE e.salary = (SELECT MAX(salary) FROM Employee)