DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS product;
DROP TABLE IF EXISTS cart;

CREATE TABLE user
(
    uid      INTEGER PRIMARY KEY UNIQUE,
    name     VARCHAR(255) NOT NULL,
    email    VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    created  TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated  TIMESTAMP             DEFAULT NULL
);

CREATE TABLE product
(
    id    INTEGER PRIMARY KEY UNIQUE,
    name  VARCHAR(255)   NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE cart
(
    id         INTEGER PRIMARY KEY UNIQUE,
    user_id    INT NOT NULL,
    product_id INT NOT NULL,
    qty        INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user (uid),
    FOREIGN KEY (product_id) REFERENCES product (id)
);
