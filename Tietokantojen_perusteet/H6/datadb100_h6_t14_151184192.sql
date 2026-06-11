-- Tietokantojen perusteet - Database basics
-- H6 T14
-- mikko.eerola@tuni.fi

SELECT artwork_name, value*(1.1) as increased_value 
FROM artwork
ORDER BY artwork_name;