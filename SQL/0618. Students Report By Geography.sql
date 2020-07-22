/*
0618. Students Report By Geography
A U.S graduate school has students from Asia, Europe and America. The students' location information are stored in table student as below.
 

| name   | continent |
|--------|-----------|
| Jack   | America   |
| Pascal | Europe    |
| Xi     | Asia      |
| Jane   | America   |
 

Pivot the continent column in this table so that each name is sorted alphabetically and displayed underneath its corresponding continent. The output headers should be America, Asia and Europe respectively. It is guaranteed that the student number from America is no less than either Asia or Europe.
 

For the sample input, the output is:
 

| America | Asia | Europe |
|---------|------|--------|
| Jack    | Xi   | Pascal |
| Jane    |      |        |
 

Follow-up: If it is unknown which continent has the most students, can you write a query to generate the student report?
*/

WITH contint AS 
(
    SELECT CASE WHEN continent = 'America' THEN name END AS America,
    CASE WHEN continent = 'Asia' THEN name END AS Asia,
    CASE WHEN continent = 'Europe' THEN name END AS Europe,
    ROW_NUMBER() OVER (PARTITION BY continent ORDER BY name) as row_num
    FROM student
)

SELECT min(America) AS america, MIN(Asia) AS Asia, MIN(Europe) AS Europe
FROM contint
GROUP BY row_num

