-- Tietokantojen perusteet - Database basics
-- H5 T3b
-- mikko.eerola@tuni.fi

SELECT technique, COUNT(*) as count
FROM artwork
GROUP BY technique;
