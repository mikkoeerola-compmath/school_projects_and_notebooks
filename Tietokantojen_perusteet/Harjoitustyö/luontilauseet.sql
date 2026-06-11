-- Tietokantojen perusteet - Database basics
-- Harjoitustyö luontilauseet
-- mikko.eerola@tuni.fi

CREATE TABLE kayttaja (
    katunnus INT,
	kanimi VARCHAR NOT NULL,
	syntymävuosi INT,
	PRIMARY KEY (katunnus),
	UNIQUE (kanimi)
	);

CREATE TABLE tuote (
    ttunnus INT,
	tnimi VARCHAR NOT NULL,
	kuvaus VARCHAR,
	hinta FLOAT,
	tmtunnus INT,
	PRIMARY KEY (ttunnus),
	UNIQUE (tnimi),
	FOREIGN KEY (tmtunnus) REFERENCES tuotemerkki
	);

CREATE TABLE tuotemerkki (
    tmtunnus INT,
	tmnimi VARCHAR NOT NULL,
	maa VARCHAR,
	PRIMARY KEY (tmtunnus),
	UNIQUE (tmnimi)
	);

CREATE TABLE arviointi (
    katunnus INT,
	ttunnus INT,
	paivamaara DATE,
	arvosana INT,
	arvio VARCHAR,
	PRIMARY KEY (katunnus, ttunnus, paivamaara),
	FOREIGN KEY (katunnus) REFERENCES kayttaja,
	FOREIGN KEY (ttunnus) REFERENCES tuote
	);

CREATE TABLE kategoria (
    ktunnus INT,
	knimi VARCHAR NOT NULL,
	PRIMARY KEY (ktunnus),
	UNIQUE (knimi)
	);

CREATE TABLE sijoittuu (
    ttunnus INT,
	ktunnus INT,
	PRIMARY KEY (ttunnus, ktunnus)
	FOREIGN KEY (ttunnus) REFERENCES tuote,
	FOREIGN KEY (ktunnus) REFERENCES kategoria
	);
