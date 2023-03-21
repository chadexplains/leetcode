SELECT DISTINCT t1.User_Id
FROM Trips t1
JOIN (
    SELECT User_Id, Car_Id
    FROM Trips
    GROUP BY User_Id, Car_Id
) t2
ON t1.User_Id = t2.User_Id AND t1.Car_Id = t2.Car_Id;