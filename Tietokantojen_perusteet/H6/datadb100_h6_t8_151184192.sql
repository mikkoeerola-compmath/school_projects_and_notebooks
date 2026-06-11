-- Tietokantojen perusteet - Database basics
-- H6 T8
-- mikko.eerola@tuni.fi

SELECT artwork_name, value, year_created, first_name, last_name
FROM artwork aw INNER JOIN artist ar ON aw.artist_id = ar.artist_id
WHERE value = (SELECT MAX(value)
			   FROM artwork);