-- Tietokantojen perusteet - Database basics
-- H1 T5
-- mikko.eerola@tuni.fi

SELECT name, price
FROM tea
WHERE price >= 6.00
ORDER BY price DESC, name;