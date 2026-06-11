-- Tietokantojen perusteet - Database basics
-- Harjoitustyö lisäyslauseet
-- mikko.eerola@tuni.fi

INSERT INTO kayttaja
VALUES (
    1, 'Anni N', 1985
);

INSERT INTO kayttaja
VALUES (
    2, 'Juuso K', 1990
);

INSERT INTO kayttaja
VALUES (
    3, 'Eino U', 1940
);

INSERT INTO kayttaja
VALUES (
    4, 'Aila J', 1953
);

INSERT INTO kategoria
VALUES (
    1, 'puutarha'
);

INSERT INTO kategoria
VALUES (
    2, 'metsa'
);

INSERT INTO kategoria
VALUES (
    3, 'lumityot'
);

INSERT INTO tuotemerkki
VALUES (
    1, 'McCee', 'Yhdysvallat'
);

INSERT INTO tuotemerkki
VALUES (
    2, 'KooTek', 'Suomi'
);

INSERT INTO tuote
VALUES (
    1, 'Trimmeri TRCee', 'tehokas 4-tahtinen', 179.00, 1
);

INSERT INTO tuote
VALUES (
    2, 'Trimmerisiima Cee', 'laadukas siima', 6.99, 1
);

INSERT INTO tuote
VALUES (
    3, 'Moottorisaha MSCee RR', 'robusti ja raskas', 559.00, 1
);

INSERT INTO tuote
VALUES (
    4, 'Trimmerisiima Y', 'yleissiima', 3.99, 2
);

INSERT INTO tuote
VALUES (
    5, 'Lapio L', 'kevyt yleislapio', 23.95, 2
);

INSERT INTO sijoittuu
VALUES (
    1, 1
);

INSERT INTO sijoittuu
VALUES (
    2, 1
);

INSERT INTO sijoittuu
VALUES (
    3, 2
);

INSERT INTO sijoittuu
VALUES (
    3, 1
);

INSERT INTO sijoittuu
VALUES (
    4, 1
);

INSERT INTO sijoittuu
VALUES (
    5, 1
);

INSERT INTO sijoittuu
VALUES (
    5, 3
);

INSERT INTO arviointi
VALUES (
    1, 1, '2021-06-05', 3, NULL
);

INSERT INTO arviointi
VALUES (
    1, 2, '2021-06-13', 2, NULL
);

INSERT INTO arviointi
VALUES (
    1, 5, '2021-07-24', 3, NULL
);

INSERT INTO arviointi
VALUES (
    1, 4, '2021-08-13', 4, NULL
);

INSERT INTO arviointi
VALUES (
    1, 1, '2021-09-12', 5, 'luotettava ja toimiva kapistus'
);

INSERT INTO arviointi
VALUES (
    3, 1, '2021-06-30', 5, 'loistava'
);

INSERT INTO arviointi
VALUES (
    3, 2, '2021-07-02', 2, 'kohtalaisesti toimii'
);

INSERT INTO arviointi
VALUES (
    2, 5, '2021-06-04', 1, 'rahastusta'	
);

INSERT INTO arviointi
VALUES (
    4, 5, '2021-08-11', 1, 'ei tee mitään'
);