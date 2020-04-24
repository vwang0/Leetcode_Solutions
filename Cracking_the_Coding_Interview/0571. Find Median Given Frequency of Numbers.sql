/*
571. Find Median Given Frequency of Numbers
The Numbers table keeps the value of number and its frequency.

+----------+-------------+
|  Number  |  Frequency  |
+----------+-------------|
|  0       |  7          |
|  1       |  1          |
|  2       |  3          |
|  3       |  1          |
+----------+-------------+
In this table, the numbers are 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 3, so the median is (0 + 0) / 2 = 0.

+--------+
| median |
+--------|
| 0.0000 |
+--------+
Write a query to find the median of all numbers and name the result as median.
*/
-- Solution 1
select avg(number) as median
from
    ( select l.number
     from numbers l
     join numbers r
     group by 1
     having abs(sum(sign(l.number - r.number) * r.frequency)) <= max(l.frequency)) t ;


/*
Key is to understand the having clause:

having abs(sum(sign(l.number - r.number) * r.frequency)) <= max(l.frequency)
Explain:
If a number is a median, it's frequency must be greater or equal than the diff of total frequency of numbers greater or less than itself.

Examples for the sub/inner query:
Example 1:

+----------+-------------+
|  Number  |  Frequency  | 
+----------+-------------|
|  0       |  5          |
|  1       |  1          |
|  2       |  5          |
+----------+-------------+
for 0, greater numbers are 1,2, total frequency is 6, 
       smaller numbers are    , total frequency is 0,
       diff is 6
       it's own frequency is 5
       5 >= 6 == false
for 1, greater numbers are 2  , total frequency is 5, 
       smaller numbers are 0  , total frequency is 5,
       diff is 0
       it's own frequency is 1
       1 >= 0 == true
for 2, same as for 0
So [1] is selected
Example 2:

+----------+-------------+
|  Number  |  Frequency  | 
+----------+-------------|
|  0       |  4          |
|  1       |  1          |
|  2       |  5          |
+----------+-------------+
for 0, greater numbers are 1,2, total frequency is 6, 
       smaller numbers are    , total frequency is 0,
       diff is 6
       it's own frequency is 4
       4 >= 6 == false
for 1, greater numbers are 2  , total frequency is 5, 
       smaller numbers are 0  , total frequency is 4,
       diff is 1
       it's own frequency is 1
       1 >= 1 == true
for 2, greater numbers are    , total frequency is 0, 
       smaller numbers are 0,1, total frequency is 5,
       diff is 5
       it's own frequency is 5
       5 >= 5 == true
So [1,2] is selected
*/

-- Solution 2

select avg(n.Number) median
from Numbers n
where n.Frequency >= abs(
                             (select sum(Frequency)
                              from Numbers
                              where Number<=n.Number) -
                             (select sum(Frequency)
                              from Numbers
                              where Number>=n.Number));

