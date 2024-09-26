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




-- EDA for Operativesystem schema
SELECT * FROM  operativsystem.tabelldata t ;

SELECT * FROM operativsystem.totalt;


SELECT
    STRFTIME('%y-%m-%d', OPTOTAL.Datum) AS Datum,
    OPTABLE.Operativsystem,
    OPTABLE.Visningar,
    OPTABLE."Visningstid (timmar)" 
FROM  
    operativsystem.tabelldata AS optable
CROSS JOIN 
    operativsystem.totalt  AS optotal
GROUP BY
    OPTABLE.Operativsystem,
    STRFTIME('%y-%m-%d', OPTOTAL.Datum), 
    OPTABLE.Visningar,
    OPTABLE."Visningstid (timmar)";



-- EDA for innerhallstyp
   
   
SELECT * FROM  geografi.diagramdata d ;
   
SELECT  * FROM  geografi.tabelldata t ;
  
SELECT * FROM  geografi.totalt t ;



SELECT
    STRFTIME('%y-%m-%d', GEO_TOT.Datum) AS Datum,
    GEO_TAB.* 
FROM  
    geografi.tabelldata AS geo_tab
CROSS JOIN
    geografi.totalt  AS geo_tot
GROUP BY
    Datum, GEO_TAB.Geografi , GEO_TAB.Visningar , GEO_TAB."Visningstid (timmar)" , GEO_TAB."Genomsnittlig visningslängd" ;











 
















