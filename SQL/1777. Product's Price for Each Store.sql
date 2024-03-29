/*
1777. Product's Price for Each Store
Easy

SQL Schema
Table: Products

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| store       | enum    |
| price       | int     |
+-------------+---------+
(product_id,store) is the primary key for this table.
store is an ENUM of type ('store1', 'store2', 'store3') where each represents the store this product is available at.
price is the price of the product at this store.
 

Write an SQL query to find the price of each product in each store.

Return the result table in any order.

The query result format is in the following example:

 

Products table:
+-------------+--------+-------+
| product_id  | store  | price |
+-------------+--------+-------+
| 0           | store1 | 95    |
| 0           | store3 | 105   |
| 0           | store2 | 100   |
| 1           | store1 | 70    |
| 1           | store3 | 80    |
+-------------+--------+-------+
Result table:
+-------------+--------+--------+--------+
| product_id  | store1 | store2 | store3 |
+-------------+--------+--------+--------+
| 0           | 95     | 100    | 105    |
| 1           | 70     | null   | 80     |
+-------------+--------+--------+--------+
Product 0 price's are 95 for store1, 100 for store2 and, 105 for store3.
Product 1 price's are 70 for store1, 80 for store3 and, it's not sold in store2.
*/
SELECT 
product_id
, MAX(if(store = "store1", price, Null)) store1
, MAX(if(store = "store2", price, Null)) store2
, MAX(if(store = "store3", price, Null)) store3
FROM Products 
GROUP BY 1


-- 2nd solution
SELECT
product_id
, MAX(CASE WHEN store = 'store1' THEN price END) AS store1
, MAX(CASE WHEN store = 'store2' THEN price END) AS store2
, MAX(CASE WHEN store = 'store3' THEN price END) AS store3
FROM Products 
GROUP BY 1