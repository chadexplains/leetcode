SELECT articles.article_id
FROM articles
LEFT JOIN views
ON articles.article_id = views.article_id
WHERE views.article_id IS NOT NULL
GROUP BY articles.article_id;