-- Tietokantojen perusteet - Database basics
-- H5 T5
-- mikko.eerola@tuni.fi

SELECT ar.artist_id, first_name, last_name
FROM artwork aw, artist ar
WHERE ar.artist_id = aw.artist_id AND technique = 'painting'
EXCEPT
SELECT ar.artist_id, first_name, last_name
FROM artist ar, artwork aw
WHERE ar.artist_id = aw.artist_id AND technique IN ('drawing', 'sculpture')
ORDER BY ar.artist_id;