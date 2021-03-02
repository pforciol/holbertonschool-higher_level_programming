-- Creates the database hbtn_0d_usa and the table states.

CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
USE `hbtn_0d_usa`;

CREATE TABLE IF NOT EXISTS `states` (
	`id` INT NOT NULL AUTO_INCREMENT UNIQUE,
	`name` VARCHAR(256) NOT NULL,
	PRIMARY KEY (`id`)
)
