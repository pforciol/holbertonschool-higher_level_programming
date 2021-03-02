-- Creates a table id_not_null table in the current database,
-- do nothing if the id_not_null table already exists.

CREATE TABLE IF NOT EXISTS `id_not_null` (
	`id` INT NOT NULL DEFAULT 1,
	`name` VARCHAR(256)
);
