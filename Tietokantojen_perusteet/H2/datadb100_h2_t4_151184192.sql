-- Tietokantojen perusteet - Database basics
-- H2 T4
-- mikko.eerola@tuni.fi

SELECT aw.artwork_id, artwork_name, technique
FROM artwork aw, exhibition ex, displayed_at dis
WHERE aw.artwork_id = dis.artwork_id and
      ex.exhibition_id = dis.exhibition_id and
	  ex.location = 'Museum of Modern Art'
ORDER BY aw.artwork_id;