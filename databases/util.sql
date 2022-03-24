-- SQL
-- Aliasing (creating inline views) to extract multiple things from same column
SELECT v.maxHigh - t.maxLow
FROM (SELECT MAX(COST) as maxHigh FROM Visit WHERE urgency = 'Highest') v, (SELECT MAX(COST) as maxLow FROM Visit WHERE urgency = 'LOWEST') t;
