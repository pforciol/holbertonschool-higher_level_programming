-- Creates the database hbtn_0d_usa and the table cities.

CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
USE `hbtn_0d_usa`;

CREATE TABLE IF NOT EXISTS `cities` (
	`id` INT NOT NULL AUTO_INCREMENT UNIQUE,
	`state_id` INT NOT NULL,
	`name` VARCHAR(256) NOT NULL,
	PRIMARY KEY (`id`),
	FOREIGN KEY (`state_id`) REFERENCES `states`(`id`)
)
