-- Tietokantojen perusteet - Database basics
-- Harjoitustyö kysely 5
-- mikko.eerola@tuni.fi

SELECT DISTINCT kanimi
FROM kayttaja ka, arviointi a , tuote t, tuotemerkki tm
WHERE ka.katunnus = a.katunnus AND a.ttunnus = t.ttunnus AND t.tmtunnus = tm.tmtunnus
    AND ka.katunnus IN (
	    SELECT katunnus
		FROM arviointi a , tuote t, tuotemerkki tm
		WHERE a.ttunnus = t.ttunnus AND t.tmtunnus = tm.tmtunnus
		AND tmnimi = 'KooTek' AND t.ttunnus = 4
	    INTERSECT
	    SELECT katunnus
		FROM arviointi a , tuote t, tuotemerkki tm
		WHERE a.ttunnus = t.ttunnus AND t.tmtunnus = tm.tmtunnus
		AND tmnimi = 'KooTek' AND t.ttunnus = 5)
ORDER BY kanimi
;