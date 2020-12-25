/*
1. given that elephant D is not an albino, what is the probability it has exactly one copy of the mutation? 2/3
2. Given that elephant E is not an albino, what is the probability it has exactly one copy of the mutation? 2/3
3. What is the probability that elephant F, when born, will be an albino?
¼ * (⅔)^2 = 1/9

4. What is the probability that elephant F, when born, will carry exactly one copy of the mutation?
½ * (⅔)^2 + (½ * ⅔ * ⅓)*2 = 4/9

5.Suppose that elephant F is born and is not an albino, Given this, what is the probability that elephant F carries exactly one copy of the mutation?
P(one|not) = [P(not|one) * P(one)] / [P(not|one) * P(one) + P(not|zero) * P(zero) + p(not|two) * P(two)]
= [1*4/9] / [1*4/9 + 1*(¼ * (⅔)^2 + (½ * ⅔ * ⅓)*2 + 1*(⅓)^2) + 0]
= ½
P(one|not) =  P(one & not) / P(not)
= 4/9 / [¾ * (⅔)^2 + (1 * ⅔ * ⅓)*2 + 1*(⅓)^2)]
= 4/9 / (1 - 1/9)
= ½

6. Suppose that elephant F is born and is not an albino. Given this, what is the probability that elephant D carries exactly one copy of the mutation?
P(D one|F not) = P(F not|D one) * P(D one) / P(F not|D zero) * P(D zero) + P(F not|D one) * P(D one) + P(F not|D two) * P(D two)
= [(¾ * ⅔ + 1 * ⅓) * ⅔] / [(¾ * ⅔ + 1 * ⅓) * ⅔ + (1*⅔ + 1*⅓) * ⅓  + 0]
= 5/8
P(D one|F not) = P(D one & F not) / P(not)
= [⅔ * (⅔*¾ + 1*⅓)] / (1 - 1/9)
= 5/8

*/

-- Robinhood
SELECT DISTINCT temp2.customer_name
(
SELECT temp1.customer_name, SUM(IF(TIME_TO_SEC(TIMEDIFF(tb.transaction_time, tb.previous_transaction_time))= 10, 1 , 0)) / COUNT(*) as cnt
FROM 
    (
    SELECT customer_name, transaction_time,
    LAG(transaction_time,1) OVER(PARTITION BY customer_name ORDER BY transaction_time) AS previous_transaction_time
    FROM customer_transactions
    ) temp1
WHERE temp1.previous_transaction_time IS NOT NULL
GROUP BY temp1.customer_name
) temp2
WHERE temp2.cnt >= 1


SELECT distinct c.name as customer_name
    FROM
    (SELECT c1.customer_name as name,
    TIMESTAMPDIFF(SECOND,c1.transaction_time,min(c2.transaction_time)) as second_diff
    FROM customer_transactions c1, customer_transactions c2
    where c1.customer_name = c2.customer_name
    and c1.transaction_time < c2.transaction_time
    group by c1.customer_name, c1.transaction_time) c
    where c.name not in (SELECT c1.customer_name as name
                         FROM customer_transactions c1, customer_transactions c2
                         where c1.customer_name = c2.customer_name
                         and c1.transaction_time < c2.transaction_time
                         group by c1.customer_name, c1.transaction_time
                        having TIMESTAMPDIFF(SECOND,c1.transaction_time,min(c2.transaction_time)) != 10)
    order by c.name;