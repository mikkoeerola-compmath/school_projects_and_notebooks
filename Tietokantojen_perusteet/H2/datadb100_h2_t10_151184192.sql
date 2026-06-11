-- Tietokantojen perusteet - Database basics
-- H2 T10
-- mikko.eerola@tuni.fi


CREATE TABLE teashop (
    shop_id INT NOT NULL,
	name VARCHAR NOT NULL,
    address VARCHAR,
	PRIMARY KEY (shop_id),
	UNIQUE (name)
);

INSERT INTO teashop
VALUES (1, 'tearoom JJ', 'Viikinkuja 2');

INSERT INTO teashop
VALUES (2, 'Koppelon tee ja turkis', 'Vätsärin tie 12');

INSERT INTO teashop
VALUES (3, 'Pyynikin kesähuone', 'Pispalan mutkatie 2');

CREATE TABLE sells (
    tea_id INT NOT NULL,
	teashop_id INT NOT NULL,
	PRIMARY KEY (teashop_id, tea_id),
	FOREIGN KEY (tea_id) REFERENCES tea(id),
	FOREIGN KEY (teashop_id) REFERENCES teashop(shop_id)
);

INSERT INTO sells
VALUES (1, 2);

INSERT INTO sells
VALUES (1, 3);

INSERT INTO sells
VALUES (2, 1);

INSERT INTO sells
VALUES (2, 2);

INSERT INTO sells
VALUES (3, 1);

INSERT INTO sells
VALUES (4, 2);

INSERT INTO sells
VALUES (4, 3);

INSERT INTO sells
VALUES (5, 1);

INSERT INTO sells
VALUES (6, 2);

INSERT INTO sells
VALUES (6, 1);
