-- displays the ave tempby city ordered by avg(descending) top 3, jul and ago.
SELECT city, avg(value) avg_temp FROM temperatures WHERE month IN (7, 8) GROUP BY city ORDER BY 2 DESC LIMIT 3;
