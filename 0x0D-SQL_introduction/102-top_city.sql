-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending) top 3, jul and ago.
SELECT city, avg(value) avg_temp FROM temperatures where month in (7,8) GROUP BY city ORDER BY 2 DESC LIMIT 3;
