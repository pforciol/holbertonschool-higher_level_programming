-- Lists the number of records with the same score in
-- the table second_table of the current database.
-- Result should display the score and the number of records
-- for this score with the label number, ordered by score.

SELECT `score`, COUNT(*) AS `number` FROM `second_table` GROUP BY `score` ORDER BY `number` DESC;
