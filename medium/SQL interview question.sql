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


/*
id | brand | revenue | cost
-----------------------------------. From 1point 3acres bbs
1 | Pizza Hut | 50.25 | 20.0
2 | Pizza Hut | 75.75 | 50.0
3 | KFC | 10.0 | 1.0
4 | Wing Street | 10.23 | 8.0

id | state
-----------
1 | WA
2 | CA
3 | CA
4 | UT

Identify the most popular brand (the brand with the largest number of stores) in each state.
*/

/*
Sample Rows in nav_events table:
user_id | event_time | event_name | session_id
Q1 - Can you write a query to calculate average dwell time in seconds across all sessions 
(i.e. return one number)? Dwell time is the length of time between opening and 
closing the menu.
Q2 - Can you write a query (or queries) to get the percentage of all sessions that 
have both nav_menu_open and nav_menu_close?
Q3 - Lets say we want to account for missing events by setting the dwell time 
to 60 seconds whenever a nav_menu_close event is missing. Can you write a query 
to re-calculate the new average dwell time when we default to 60 seconds of dwell time 
whenever nav_menu_close is missing?
*/
-- Q1
SELECT AVG(DATEDIFF(SECOND, t2.event_time, t1.event_time))
FROM nav_event t1
JOIN nav_event t2 ON 
t1.session_id = t2.session_id
WHERE t2.event_name = 'close'
AND t1.event_name = 'open'
-- Q2
SELECT (
    SELEC COUNT(*) FROM table nav_event t1
    JOIN nav_event t2
    ON t1.session_id = t2.session_id
    WHERE t2.event_name = 'close' 
    AND t1.event_name = 'open' ) / COUNT(*)
FROM nav_event
-- Q3
SELECT AVG(IFNULL(DATEDIFF(seconds, a.event_name, b.event_name),60)
FROM nav_event a
LEFT JOIN nav_event b 
ON a.session_id=b.session_id
WHERE a.event_name=’open’
AND b.event_name=’close’


/*
SQL题是user_action和post两个table
user_action  
ds | actor_Id | post_id | relationship(friend, page, group) |interaction(like, comment,wow)

user_post
ds | poster_id |post_id

1. 找出昨天朋友之间like的总数
2. 找出用户为123的收到的like的比例
*/