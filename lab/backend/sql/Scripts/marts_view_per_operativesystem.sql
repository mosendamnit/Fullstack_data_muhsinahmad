CREATE TABLE IF NOT EXISTS marts.operativesystem_per_view AS
(
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
    OPTABLE."Visningstid (timmar)"
);

CREATE TABLE IF NOT EXISTS marts.views_per_geografi AS 
(
SELECT
    STRFTIME('%y-%m-%d', GEO_TOT.Datum) AS Datum,
    GEO_TAB.* 
FROM  
    geografi.tabelldata AS geo_tab
CROSS JOIN
    geografi.totalt  AS geo_tot
GROUP BY
    Datum, GEO_TAB.Geografi , GEO_TAB.Visningar , GEO_TAB."Visningstid (timmar)" , GEO_TAB."Genomsnittlig visningslängd"

);

SELECT * FROM marts.operativesystem_per_view;

SELECT * FROM marts.views_per_geografi vpg ;