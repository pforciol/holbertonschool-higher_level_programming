-- Lists all records in the table second_table of the current database.
-- Result should display the score and the name, ordered by score.

SELECT `score`, `name` FROM `second_table` WHERE `name` IS NOT NULL ORDER BY `score` DESC;
