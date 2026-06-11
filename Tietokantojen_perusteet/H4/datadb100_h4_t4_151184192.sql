-- Tietokantojen perusteet - Database basics
-- H4 osa2 T4
-- mikko.eerola@tuni.fi


SELECT technique, artwork_name, last_name
FROM artist as ar INNER JOIN artwork as aw ON 
    ar.artist_id = aw.artist_id
WHERE technique = 'sculpture' OR technique = 'drawing'
ORDER BY technique, artwork_name;