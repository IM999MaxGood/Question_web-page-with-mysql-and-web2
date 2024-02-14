CREATE DATABASE IF NOT EXISTS web_page_mysql2;

USE web_page_mysql2;

CREATE TABLE item(
    id INT AUTO_INCREMENT,
    title TEXT,
    PRIMARY KEY (id)
);

CREATE USER 'im999maxgood_U'@'localhost' IDENTIFIED BY '123456';

GRANT ALL PRIVILEGES ON web_page_mysql2.* TO 'im999maxgood_U'@'localhost';

