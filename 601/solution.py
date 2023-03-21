SELECT t1.id, t1.visit_date, t1.people
FROM stadium t1
JOIN stadium t2
ON t1.id = t2.id - 1
AND t1.people >= 100
AND t2.people >= 100
JOIN stadium t3
ON t1.id = t3.id - 2
AND t1.people >= 100
AND t3.people >= 100
GROUP BY t1.id, t2.id
HAVING COUNT(*) >= 2;