-- Tietokantojen perusteet - Database basics
-- Harjoitustyö kysely 2
-- mikko.eerola@tuni.fi

SELECT syntymavuosi, kanimi
FROM kayttaja ka
WHERE ka.katunnus IN 
    (SELECT ka.katunnus
	 FROM tuotemerkki tm, tuote t, arviointi ar, kayttaja ka
	 WHERE tm.tmtunnus = t.tmtunnus AND
     ar.katunnus = ka.katunnus AND ar.ttunnus = t.ttunnus
	 AND tmnimi = 'KooTek')
	AND
	ka.katunnus IN
	(SELECT ka.katunnus
	 FROM tuotemerkki tm, tuote t, arviointi ar, kayttaja ka
	 WHERE tm.tmtunnus = t.tmtunnus AND
     ar.katunnus = ka.katunnus AND ar.ttunnus = t.ttunnus
	 AND tmnimi = 'McCee')
ORDER BY syntymavuosi, kanimi;