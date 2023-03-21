SELECT f1.follower follower_id, f1.followee followee_id
FROM follow f1
LEFT JOIN follow f2
ON f1.follower = f2.followee AND f1.followee = f2.follower
WHERE f2.follower IS NULL;