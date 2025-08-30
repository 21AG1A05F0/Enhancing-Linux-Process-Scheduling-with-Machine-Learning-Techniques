DROP DATABASE IF EXISTS linux;
CREATE DATABASE linux;
USE linux;

CREATE TABLE `users` (
    `name` VARCHAR(225),
    `email` VARCHAR(225),
    `password` VARCHAR(225),
    `phonenumber` VARCHAR(225),`age` VARCHAR(225)
    )