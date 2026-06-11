-- Tietokantojen perusteet - Database basics
-- H5 T1
-- mikko.eerola@tuni.fi

SELECT artwork_name, technique
FROM artwork
WHERE technique IN ('painting', 'drawing')
ORDER BY technique, artwork_name;