-- Tietokantojen perusteet - Database basics
-- H2 T8
-- mikko.eerola@tuni.fi

SELECT aw.artwork_id, aw.artwork_name, ex.exhibition_id,
    ex.exhibition_name, ex.year
FROM ((artwork aw OUTER LEFT JOIN displayed_at dis 
    ON aw.artwork_id = dis.artwork_id) OUTER LEFT JOIN
	exhibition ex ON dis.exhibition_id = ex.exhibition_id)
ORDER BY aw.artwork_id, ex.exhibition_id;