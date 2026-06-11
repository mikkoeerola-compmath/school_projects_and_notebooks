-- Tietokantojen perusteet - Database basics
-- H6 T1
-- mikko.eerola@tuni.fi

SELECT artwork_id, artwork_name
FROM artwork
WHERE EXISTS (
    SELECT artwork_id
	FROM displayed_at
	WHERE artwork.artwork_id = displayed_at.artwork_id)
ORDER BY artwork_id;

