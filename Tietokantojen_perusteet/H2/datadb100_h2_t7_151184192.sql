-- Tietokantojen perusteet - Database basics
-- H2 T7
-- mikko.eerola@tuni.fi

SELECT a.first_name, a.last_name, a.artist_id, aw.artwork_id,
    aw.artwork_name
FROM artist a LEFT OUTER JOIN artwork aw
    ON a.artist_id = aw.artist_id
ORDER BY a.artist_id, aw.artwork_id;