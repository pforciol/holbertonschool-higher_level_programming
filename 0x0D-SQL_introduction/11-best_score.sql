-- Lists all records with a score >= 10 of the
-- table second_table of the current database.
-- Result should display both the score and the name, ordered by score.

SELECT `score`, `name` FROM `second_table` WHERE `score` >= 10 ORDER BY `score` DESC;
