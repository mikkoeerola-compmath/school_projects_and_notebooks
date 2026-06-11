-- Tietokantojen perusteet - Database basics
-- H2 T3
-- mikko.eerola@tuni.fi

SELECT artwork_id, artwork_name, first_name, last_name, year_created
FROM artwork, artist
WHERE artist.artist_id = artwork.artist_id and technique = 'painting'
ORDER BY artwork_id;