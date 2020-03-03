-- show cities of california
-- not allowed to use the JOIN keyword
SELECT id, name FROM cities WHERE state_id in (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
