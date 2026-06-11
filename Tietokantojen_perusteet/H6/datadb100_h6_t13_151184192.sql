-- Tietokantojen perusteet - Database basics
-- H6 T13
-- mikko.eerola@tuni.fi

SELECT artwork_name
FROM artwork
WHERE year_created BETWEEN 1500 and 1600
ORDER BY artwork_name;