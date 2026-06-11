-- T1.2
-- Eerola Mikko 151184192

SELECT yl.yarn_id, yarn_name
FROM yarn_label yl, material m, yarn_material ym
WHERE yl.yarn_id = ym.yarn_id AND m.material_id = ym.material_id
    AND material_name = 'wool' AND percentage = 100
ORDER BY yl.yarn_id;