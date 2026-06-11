-- T1.3
-- Eerola Mikko 151184192

SELECT manufacturer_name, COUNT(DISTINCT yl.yarn_id) AS no_yarn_labels,
    COUNT(DISTINCT material_id) as no_material, MAX(skein_price) as highest_price
FROM (manufacturer mf LEFT OUTER JOIN yarn_label yl ON
    mf.manufacturer_id = yl.manufacturer_id) LEFT OUTER JOIN yarn_material ym
	ON yl.yarn_id = ym.yarn_id
GROUP BY mf.manufacturer_name
ORDER BY mf.manufacturer_name;