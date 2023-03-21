SELECT e1.Company_Id, AVG(e1.Salary) AS Median
FROM Employee e1
JOIN Employee e2
ON e1.Company_Id = e2.Company_Id
GROUP BY e1.Company_Id
HAVING COUNT(*) >= ABS(SUM(SIGN(1-SIGN(e1.Salary-e2.Salary))))
AND COUNT(*) <= ABS(SUM(SIGN(1+SIGN(e1.Salary-e2.Salary))))+1;