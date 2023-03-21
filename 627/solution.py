UPDATE salary
SET salary =
CASE
    WHEN id = (SELECT id FROM salary ORDER BY salary LIMIT 1)
        THEN (SELECT salary FROM salary ORDER BY salary LIMIT 1 OFFSET 1)
    ELSE (SELECT salary FROM salary ORDER BY salary LIMIT 1)
END;