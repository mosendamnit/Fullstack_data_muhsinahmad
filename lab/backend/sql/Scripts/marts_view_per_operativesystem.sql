CREATE TABLE IF NOT EXISTS marts.operativesystem_per_view AS
(
SELECT
    STRFTIME('%Y-%m-%d', optotal."Datum") AS Datum,
    optable."Operativsystem",
    SUM(optable."Visningar") AS Total_Visningar,
    SUM(optable."Visningstid (timmar)") AS Total_Visningstid_timmar
FROM  
    operativsystem.tabelldata AS optable
CROSS JOIN 
    operativsystem.totalt AS optotal
GROUP BY
    STRFTIME('%Y-%m-%d', optotal."Datum"),
    optable."Operativsystem"
ORDER BY
    STRFTIME('%Y-%m-%d', optotal."Datum"),
    optable."Operativsystem"
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