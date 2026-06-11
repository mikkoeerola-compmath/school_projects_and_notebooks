-- Tietokantojen perusteet - Database basics
-- H5 T4b
-- mikko.eerola@tuni.fi

SELECT ar.artist_id, first_name, last_name, COUNT(artwork_id)
    AS artwork_count, MIN(value) as min_value, MAX(value) as max_value
FROM artwork aw, artist ar
WHERE ar.artist_id = aw.artist_id
GROUP BY ar.artist_id, first_name, last_name
ORDER BY ar.artist_id;
