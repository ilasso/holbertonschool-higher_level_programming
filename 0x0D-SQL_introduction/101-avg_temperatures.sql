-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT city, avg(value) avg_temp FROM temperatures GROUP BY city ORDER BY 2 DESC;
