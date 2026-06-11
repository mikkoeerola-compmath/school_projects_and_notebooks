-- Tietokantojen perusteet - Database basics
-- H5 T7
-- mikko.eerola@tuni.fi

SELECT aw.artwork_id, artwork_name, technique
FROM ((artwork aw LEFT OUTER JOIN displayed_at dis ON 
    aw.artwork_id = dis.artwork_id) LEFT OUTER JOIN exhibition ex ON
    ex.exhibition_id = dis.exhibition_id)
GROUP BY aw.artwork_id, artwork_name, technique
HAVING COUNT(ex.exhibition_id) = 1
ORDER BY aw.artwork_id;
