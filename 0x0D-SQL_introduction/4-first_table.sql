-- Creates a table first_table table in the current database,
-- do nothing if the first_table table already exists.

CREATE TABLE IF NOT EXISTS `first_table` (
	`id` INT,
	`name` VARCHAR(256)
);
