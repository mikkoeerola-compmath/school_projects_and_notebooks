-- T1.1
-- Eerola Mikko 151184192

SELECT yarn_id, yarn_name, manufacturer_name, web_address
FROM yarn_label yl, manufacturer mf
WHERE yl.manufacturer_id = mf.manufacturer_id AND skein_price >= 5.0
   AND web_address NOT NULL
ORDER BY yarn_id;