-- Tietokantojen perusteet - Database basics
-- H2 T9
-- mikko.eerola@tuni.fi

SELECT aw.artwork_id, aw.artwork_name
FROM (artwork aw LEFT OUTER JOIN displayed_at dis
    ON aw.artwork_id = dis.artwork_id)
WHERE dis.exhibition_id IS NULL
ORDER BY aw.artwork_id;
