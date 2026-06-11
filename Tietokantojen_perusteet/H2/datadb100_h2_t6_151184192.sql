-- Tietokantojen perusteet - Database basics
-- H2 T6
-- mikko.eerola@tuni.fi

SELECT DISTINCT aw.artwork_id, aw.artwork_name
FROM artwork aw, displayed_at dis
WHERE aw.artwork_id = dis.artwork_id
ORDER BY aw.artwork_id;