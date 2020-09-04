/*
table: customer_info
email permutations
SQL 1
原始数据：
user_id, email
1           email1@gmail.com
1           email2@gmail.com
1           email3@gmail.com
2           email1@gmail.com
2           email2@gmail.com

要求 : 列出每个 ID的所有email组合  不重复
user_id email1, email2
1 email1@gmail.com, email2@gmail.com
1 email1@gmail.com, email3@gmail.com
1 email2@gmail.com, email3@gmail.com
2 email1@gmail.com, email2@gmail.com

*/
SELECT a.user_id, a.email AS email1, b.eamil AS email2
FROM customer_info a
JOIN customer_info b
WHERE a.user_id = b.user_id AND a.email != b.email