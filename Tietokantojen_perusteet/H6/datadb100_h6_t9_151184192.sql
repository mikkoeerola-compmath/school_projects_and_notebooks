-- Tietokantojen perusteet - Database basics
-- H6 T9
-- mikko.eerola@tuni.fi

SELECT technique
FROM artwork
GROUP BY technique
HAVING AVG(value) > (SELECT AVG(value)
					 FROM artwork);