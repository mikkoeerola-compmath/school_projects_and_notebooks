-- T1.4
-- Eerola Mikko 151184192

SELECT yla.yarn_id, yla.yarn_name, ylb.yarn_id, ylb.yarn_name
FROM yarn_label yla, yarn_label ylb, material m, yarn_material yma,
    yarn_material ymb
WHERE yla.yarn_id = yma.yarn_id AND yma.material_id = m.material_id AND
    ylb.yarn_id = ymb.yarn_id AND ymb.material_id = m.material_id AND
	yma.material_id = ymb.material_id
GROUP BY yla.yarn_id
HAVING COUNT(*) > 2
ORDER BY yla.yarn_id, ylb.yarn_id;
