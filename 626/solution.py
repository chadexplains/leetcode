SELECT IFNULL((SELECT s2.id FROM seat s2 WHERE s2.id = s1.id + 1), s1.id) AS id, s1.student FROM seat s1 ORDER BY s1.id ASC;