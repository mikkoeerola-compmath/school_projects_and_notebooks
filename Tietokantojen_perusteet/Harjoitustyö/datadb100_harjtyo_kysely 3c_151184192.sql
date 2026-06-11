-- Tietokantojen perusteet - Database basics
-- Harjoitustyö kysely 3c
-- mikko.eerola@tuni.fi

SELECT tnimi, hinta
FROM tuote, tuotemerkki
WHERE tuote.tmtunnus = tuotemerkki.tmtunnus AND tmnimi = 'McCee'
    AND hinta = (
	    select MIN(hinta)
		FROM tuote, tuotemerkki
		WHERE tuote.tmtunnus = tuotemerkki.tmtunnus AND tmnimi = 'McCee')
;