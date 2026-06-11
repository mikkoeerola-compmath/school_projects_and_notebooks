-- Tietokantojen perusteet - Database basics
-- H6 T10
-- mikko.eerola@tuni.fi

SELECT ar.artist_id, first_name, last_name, 
    COUNT(aw.artwork_id) as created_artwork, exhibitions
FROM artist ar outer left join (artwork aw inner join
	(SELECT aw.artwork_id, COUNT(exhibition_id) as exhibitions
     FROM artwork aw outer left join displayed_at dis ON
     aw.artwork_id = dis.artwork_id
     GROUP BY aw.artwork_id) as artinfo ON
	aw.artwork_id = artinfo.artwork_id)
	ON ar.artist_id = aw.artist_id
GROUP BY ar.artist_id;
