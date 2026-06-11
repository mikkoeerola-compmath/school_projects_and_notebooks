-- T2
-- Eerola Mikko 151184192

CREATE TABLE color (
    color_id INT,
	color VARCHAR NOT NULL,
	no_in_stock INT,
	PRIMARY KEY (color_id),
	UNIQUE (color)
	);

CREATE TABLE yarn_color (
    yarn_id INT,
	color_id INT NOT NULL,
	PRIMARY KEY (yarn_id, color_id),
	FOREIGN KEY (yarn_id) REFERENCES yarn_label,
	FOREIGN KEY (color_id) REFERENCES color
	);