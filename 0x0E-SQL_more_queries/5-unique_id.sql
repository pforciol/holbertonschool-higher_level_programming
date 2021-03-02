-- Creates a table unique_id table in the current database,
-- do nothing if the unique_id table already exists.

CREATE TABLE IF NOT EXISTS `unique_id` (
	`id` INT NOT NULL DEFAULT 1 UNIQUE,
	`name` VARCHAR(256)
);
