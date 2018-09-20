use scraping;
CREATE TABLE pages (
id BIGINT(7) NOT NULL AUTO_INCREMENT,
title VARCHAR(200),
content VARCHAR(10000),
created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY(id)
);

INSERT INTO pages (title, content) VALUES ("Test page title", "This is some test page content. It can be up to 10,000 characters long.");

