SELECT d.Name as Department, e.Name as Employee
FROM
(SELECT DepartmentId, Name, Salary, RANK() OVER (PARTITION BY DepartmentId ORDER BY Salary DESC) as rank
FROM Employee) e
JOIN Department d ON e.DepartmentId = d.Id
WHERE e.rank <= 3;