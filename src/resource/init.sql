SET collation_connection = 'utf8_general_ci';

ALTER DATABASE newsfeed CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

DROP TABLE news;

CREATE TABLE news (
    id int NOT NULL AUTO_INCREMENT,
    title varchar(255) NOT NULL,
    newsLink varchar(510) NOT NULL,
    imageLink varchar(1000),
    postDateTime varchar(255) NOT NULL,
    catalogue varchar(255),
    organization VARCHAR(255),
    PRIMARY KEY (id)
) ENGINE=InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;

