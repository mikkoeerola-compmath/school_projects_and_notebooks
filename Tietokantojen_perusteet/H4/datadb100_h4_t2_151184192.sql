-- Tietokantojen perusteet - Database basics
-- H4 osa2 T2
-- mikko.eerola@tuni.fi


SELECT artwork_id, value, year_created
FROM artwork as art
WHERE  value < 50000 AND year_created > 1510
ORDER BY artwork_id;