-- Tietokantojen perusteet - Database basics
-- Harjoitustyö kysely 4b
-- mikko.eerola@tuni.fi

SELECT tnimi, MIN(arvosana) as min_arvosana, MAX(arvosana) as max_arvosana,
    AVG(arvosana) as ka_arvosana, COUNT(arvosana) as lkm_arvosana, COUNT(distinct kanimi)
	as eri_kayttajia
FROM (tuote LEFT OUTER JOIN arviointi ON tuote.ttunnus = arviointi.ttunnus)
    LEFT OUTER JOIN kayttaja ON arviointi.katunnus = kayttaja.katunnus
GROUP BY tuote.ttunnus
ORDER BY tnimi;
