SELECT e.tipo , COUNT(a.id) as quantidade
FROM atletas a
INNER JOIN atletas_eventos ae 
ON  a.id = ae.atletas_id
INNER JOIN evento e 
ON ae.evento_id = e.id
GROUP BY a.id ,e.tipo

