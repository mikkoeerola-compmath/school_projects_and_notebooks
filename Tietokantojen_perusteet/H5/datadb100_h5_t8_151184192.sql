-- Tietokantojen perusteet - Database basics
-- H5 T8
-- mikko.eerola@tuni.fi

SELECT aw.artwork_id, artwork_name, technique, first_name, last_name
FROM artist ar, ((artwork aw LEFT OUTER JOIN displayed_at dis ON 
    aw.artwork_id = dis.artwork_id) LEFT OUTER JOIN exhibition ex ON
    ex.exhibition_id = dis.exhibition_id)
WHERE ar.artist_id = aw.artist_id
GROUP BY aw.artwork_id, artwork_name, technique
HAVING COUNT(ex.exhibition_id) = 1
ORDER BY aw.artwork_id;

