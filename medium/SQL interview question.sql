/*
find employees reporting to the managers whose first name is John
Employee table: 
employee_name  | employee_id | manager_id
John Smith     |    34              2
Sara Thompson  |    52              34
Rachel Sanders |    22              2
John Adams     |    2               NULL 
output:
employee_name   |   report_to
John Smith          John Adams
Rachel Sanders      John Adams
*/

SELECT emp.employee_name AS employee_name, mgr.employee_name AS report_to
FROM Employee AS emp
LEFT JOIN Employee AS mgr 
WHERE report_to LIKE 'John *'
ON emp.manager_id = mgr.employee_id
