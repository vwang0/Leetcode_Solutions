
select user_id,user_name, IFNULL((credit + sum(profit)),credit) as credit,
case when credit+ sum(profit) < 0 then 'Yes' else 'No' end as credit_limit_breached
FROM(
SELECT
user_id,
user_name,
u.credit,
case when user_id = t1.paid_by then -t1.amount end as profit
FROM users u
LEFT JOIN transactions t1 on u.user_id = t1.paid_by
UNION
SELECT
user_id,
user_name,
u.credit,
case when user_id = t2.paid_to then t2.amount end as profit
FROM users u
LEFT JOIN transactions t2 on u.user_id = t2.paid_to)t
GROUP BY user_id

SELECT U.user_id, user_name, IFNULL(credit+amt2, credit) 'credit', (CASE WHEN IFNULL(credit+amt2, credit)>=0 THEN 'No' ELSE 'Yes' END) credit_limit_breached 
FROM Users U
LEFT JOIN

(SELECT user_id, sum(amt) amt2
FROM
(SELECT paid_by user_id, -sum(amount) amt
FROM Transactions 
GROUP BY paid_by

UNION ALL

SELECT paid_to user_id, sum(amount) amt
FROM Transactions 
GROUP BY paid_to) t1

GROUP BY user_id) t2

ON U.user_id = t2.user_id