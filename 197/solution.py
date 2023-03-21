SELECT w1.Id
FROM Weather w1
JOIN Weather w2
ON DATEDIFF(w1.Date, w2.Date) = 1
AND w1.Temperature > w2.Temperature;