-- Creates a table force_name table in the current database,
-- do nothing if the force_name table already exists.

CREATE TABLE IF NOT EXISTS `force_name` (
	`id` INT,
	`name` VARCHAR(256) NOT NULL
);
