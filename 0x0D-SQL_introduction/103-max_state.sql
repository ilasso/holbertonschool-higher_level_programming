-- displays the max temperature of each state (ordered by State name)
SELECT state, max(value) max_temp FROM temperatures GROUP BY state order by 1;
