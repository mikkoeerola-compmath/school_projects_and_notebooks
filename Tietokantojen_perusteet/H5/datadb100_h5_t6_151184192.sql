-- Tietokantojen perusteet - Database basics
-- H5 T6
-- mikko.eerola@tuni.fi

SELECT aw.artwork_id, artwork_name, COUNT(ex.exhibition_id) as exhibition_count
FROM ((artwork aw LEFT OUTER JOIN displayed_at dis ON 
    aw.artwork_id = dis.artwork_id) LEFT OUTER JOIN exhibition ex ON
    ex.exhibition_id = dis.exhibition_id)
GROUP BY aw.artwork_id, artwork_name
ORDER BY aw.artwork_id;
