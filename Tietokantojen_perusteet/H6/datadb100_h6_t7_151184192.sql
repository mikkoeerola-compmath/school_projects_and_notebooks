-- Tietokantojen perusteet - Database basics
-- H6 T7
-- mikko.eerola@tuni.fi

SELECT artwork_name, value, year_created
FROM artwork
WHERE value = (SELECT MAX(value)
			   FROM artwork);