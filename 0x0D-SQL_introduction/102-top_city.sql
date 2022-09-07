-- Using temperature data set from ex.18
-- Display top 3 cities by temperature during July and August
-- ordered by temperature descending
SELECT city, AVG(value) as avg_temp FROM temperatures WHERE month = 8 OR month = 7
GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
