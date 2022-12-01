-- A script to list all records of a table with a particular field
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
