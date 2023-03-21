SELECT article_id
FROM Views
WHERE views = (SELECT MAX(views) FROM Views)
ORDER BY article_id ASC;