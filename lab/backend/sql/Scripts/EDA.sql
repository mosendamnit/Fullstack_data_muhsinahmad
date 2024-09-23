WITH 
	date_table AS (SELECT * FROM datum.tabelldata OFFSET 1),
	date_total AS (SELECT * FROM datum.totalt OFFSET 1)
SELECT 
	STRFTIME('%Y-%m-%d', tot.datum), 
	tot.visningar,
	tab.visningar,
	tab."visningstid (timmar)"
FROM date_total as tot
LEFT JOIN date_table as tab 
ON tot.datum = tab.datum;



SELECT Enhetstyp, count(*) total_rows, sum(Visningar) as total_visningar 
from 
enhetstyp.diagramdata group by Enhetstyp ;

select * from enhetstyp.diagramdata;

SELECT * EXCLUDE (Innehåll) FROM  innehall.tabelldata ORDER BY "Visningstid (timmar)" DESC OFFSET 1 LIMIT 5;

SELECT * FROM  innehall.diagramdata;-- ORDER BY "Visningstid (timmar)";

SELECT STRFTIME('%Y-%m-%d', Datum), Visningar FROM innehall.totalt;


-- Do some EDA for Operativesystem schema


-- Print Daigrammdata in Operativesystem Scheam

SELECT * FROM  operativsystem.diagramdata d ;

SELECT
	STRFTIME('%y-%m-%d' ,
	Datum) AS Datum ,
	Operativsystem ,
	Visningar
FROM
	operativsystem.diagramdata
ORDER BY
	Datum DESC;


-- Print tabledata in Operativesystem Schema

SELECT * EXCLUDE("Genomsnittlig visningslängd") FROM operativsystem.tabelldata;


-- Print totaldata in Operativesystem Schema

SELECT * FROM operativsystem.totalt t ;


WITH operative_table AS (SELECT * FROM operativsystem.tabelldata),
     operative_total AS (SELECT * FROM operativsystem.totalt)
SELECT
    STRFTIME('%y-%m-%d', ototal.Datum) AS Datum,
    otable.*
FROM
    operative_total AS ototal
LEFT JOIN operative_table AS otable
ON ototal.Datum = otable.Operativsystem;






SELECT * FROM tittare.tabelldata_alder ta ;

SELECT * FROM  tittare.tabelldata_kon tk ;

WITH tittare_table AS (
SELECT
	*
FROM
	tittare.tabelldata_alder ta) ,
tittare_total AS (
SELECT
	*
FROM
	tittare.tabelldata_kon tk)
SELECT
	 Visningar(%) AS Visningar
FROM
	tittare_total AS tit_tot
LEFT JOIN tittare_table AS tit_tab
ON tit_tot.Visningar = tit_tab.Visningar;








