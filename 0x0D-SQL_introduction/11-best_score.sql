-- list all records whith score >= 10 in a table of a database in a server.
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
