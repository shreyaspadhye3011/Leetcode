CREATE VIEW YEAR_VIEW AS 
SELECT M1.YEAR, COUNT(*) AS CNT
FROM MOVIE M1, MOVIE M2
WHERE M2.YEAR >= M1.YEAR AND M2.YEAR < M1.YEAR +10 
GROUP BY M1.YEAR;

SELECT YEAR 
FROM YEAR_VIEW
WHERE CNT = (SELECT MAX(CNT) FROM YEAR_VIEW);