-- Tietokantojen perusteet - Database basics
-- H6 T5
-- mikko.eerola@tuni.fi

SELECT artist_id, first_name, last_name
FROM artist
WHERE artist_id IN
    (SELECT artist_id
	FROM artwork
	WHERE technique = 'drawing')
	AND artist_id IN
	(SELECT artist_id
	FROM artwork
	WHERE technique = 'painting')
ORDER BY artist_id;