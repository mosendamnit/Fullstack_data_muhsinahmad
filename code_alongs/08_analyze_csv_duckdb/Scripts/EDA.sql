SELECT * FROM  youtube;


SELECT DISTINCT category from youtube;

SELECT COUNT(category)  FROM youtube WHERE category = 'Science & Technology';

SELECT COUNT(*) from youtube;

-- how many in each category

SELECT  category , count(*) AS Number FROM youtube GROUP BY category ORDER BY number DESC LIMIT 10 ;


SELECT "youtuber name" , category FROM youtube WHERE category = 'Science & Technology';

SELECT * FROM  youtube;

SELECT "youtuber name" , category FROM youtube WHERE "Audience Country" = 'Pakistan';

SELECT * EXCLUDE("avg views" , "avg comments" , "avg likes") FROM youtube WHERE "Audience Country" = 'Pakistan';

SELECT * FROM  youtube;

SELECT "Audience Country" from youtube;

SELECT * from youtube WHERE "audience country" = 'Japan';

SELECT category ,  COUNT("audience country") AS country_count from youtube Group by category ORDER BY  country_count DESC; 