-- Tietokantojen perusteet - Database basics
-- H2 T5
-- mikko.eerola@tuni.fi

SELECT ex.year, ex.exhibition_name, a.first_name, 
    a.last_name, aw.artwork_name
FROM artwork aw, exhibition ex, displayed_at dis, artist a
WHERE aw.artwork_id = dis.artwork_id
    AND a.artist_id = aw.artist_id
	AND ex.exhibition_id = dis.exhibition_id
ORDER BY ex.year, a.last_name, aw.artwork_name;