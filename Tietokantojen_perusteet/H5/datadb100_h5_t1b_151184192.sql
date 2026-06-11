-- Tietokantojen perusteet - Database basics
-- H5 T1b
-- mikko.eerola@tuni.fi

SELECT COUNT(*) as artwork_count, MIN(value) as min_value,
    MAX(value) as max_value
FROM artwork;

