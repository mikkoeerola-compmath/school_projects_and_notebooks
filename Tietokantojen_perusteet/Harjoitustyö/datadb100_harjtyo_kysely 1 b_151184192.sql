-- Tietokantojen perusteet - Database basics
-- Harjoitustyö kysely 1B
-- mikko.eerola@tuni.fi

SELECT tmnimi, tnimi, paivamaara, arvosana
FROM tuotemerkki tm, tuote t, arviointi ar, kayttaja ka
WHERE kanimi = 'Anni N' AND tm.tmtunnus = t.tmtunnus AND
    ar.katunnus = ka.katunnus AND ar.ttunnus = t.ttunnus
ORDER BY tm.tmnimi, tnimi, paivamaara DESC;