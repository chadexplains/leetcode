SELECT DISTINCT a.num AS ConsecutiveNums
FROM nums a, nums b, nums c
WHERE a.num = b.num AND b.num = c.num AND a.id = b.id - 1 AND b.id = c.id - 1;