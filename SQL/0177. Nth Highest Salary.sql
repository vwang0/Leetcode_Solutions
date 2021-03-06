/*
177. Nth Highest Salary
Write a SQL query to get the nth highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
For example, given the above Employee table, the nth highest salary where n = 2 is 200. If there is no nth highest salary, then the query should return null.

+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+
*/
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    RETURN (
        SELECT MAX(Salary)
        FROM Employee AS E1
        WHERE N = (
            SELECT COUNT(DISTINCT(E2.Salary)) 
            FROM Employee AS E2
            WHERE E2.Salary >= E1.Salary
        ) 
  );
END


CREATE FUNCTION  getNthHighestSalary(N INT) RETURNS INT
BEGIN
    RETURN 
    (
        WITH temp AS 
        (
            SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS salary_rank
            FROM Employee
        ) 

        SELECT DISTINCT salary
        FROM temp
        WHERE salary_rank = N


    );
END

