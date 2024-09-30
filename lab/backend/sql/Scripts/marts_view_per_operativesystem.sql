-- Mart For  Views details as per Operative System. 

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

SELECT * FROM marts.operativesystem_per_view opv ;


-- Mart for Views details as per geografic (state)

CREATE TABLE IF NOT EXISTS marts.views_per_geografi AS 
(
SELECT 
    STRFTIME('%y-%m-%d', geo_dia.Datum) AS Datum,
    GROUP_CONCAT(DISTINCT geo_dia.Geografi) AS Geografi,
    MAX(geo_tot.Visningar) AS Total_Viewers
FROM 
    geografi.diagramdata AS geo_dia
LEFT JOIN
    geografi.totalt AS geo_tot
ON
    geo_dia.Datum = geo_tot.Datum
GROUP BY 
    geo_dia.Datum
ORDER BY 
    geo_dia.Datum
);


SELECT * FROM marts.views_per_geografi ;