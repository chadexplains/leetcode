SELECT e.Name
FROM Employee e
JOIN Salary s
ON e.Id = s.Id
WHERE s.Salary < (SELECT MAX(Salary) FROM Salary)