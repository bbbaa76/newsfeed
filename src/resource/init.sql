SET collation_connection = 'utf8_general_ci';

DROP DATABASE newsfeed;

CREATE DATABASE newsfeed CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

GRANT ALL ON newsfeed.* to 'anthony'@'localhost';

use newsfeed;

CREATE TABLE news (
    id int NOT NULL AUTO_INCREMENT,
    title varchar(255) NOT NULL,
    news_link varchar(510) NOT NULL,
    image_link varchar(510),
    post_date_time varchar(255) NOT NULL,
    catalogue varchar(255),
    organization varchar(255),
    PRIMARY KEY (id)
) ENGINE=InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;

