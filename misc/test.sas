proc sort data = data1; by id; run;
proc sort data = data2; by id; run;

data matchdata;
merge data1 data2;
by id;
run;
proc print matchdata;
run

data solution;
merge many(drop = state) one;
by id;
run;

proc sql;
select s.*, d.*
from s, d
where s.flight = d.flight;


coalesce(car1, var2)

coalesce

proc sql;

CREATE TABLE BOTH AS

SELECT A.PATIENT,
A.DATE FORMAT=DATE7. AS DATE,
A.PULSE,B.MED, B.DOSES,
B.AMT FORMAT=4.1

FROM VITALS A 
INNER JOIN DOSING B
ON (A.PATIENT = B.PATIENT)
AND(A.DATE = B.DATE)
ORDER BY PATIENT, DATE;
QUIT;



PROC SQL;
CREATE TABLE HIGHBPP2 AS
SELECT PATIENT,
COUNT (PATIENT) AS N,
DATE FORMAT=DATE7.,
MAX(BPD) AS BPDHIGH
FROM VITALS
WHERE PATIENT IN (101 102 103)
GROUP BY PATIENT
HAVING BPD = CALCULATED BPDHIGH
ORDER BY caluculated BPDHIGH;
Quit;



data tot;
set calc;
if 3<=id<=8 then 
total + marks;
if id = 8 then put total = ;
run;
