/*
https://www.1point3acres.com/bbs/thread-529697-1-1.html
https://medium.com/jbennetcodes/how-to-rewrite-your-sql-queries-in-pandas-and-more-149d341fc53e
*/

-- Python pandas
/*
member_spend[member_spend.mobile_spend>0 & member_spend.desktop_spend==0], ‘channel’] = ‘mobile’
member_spend[member_spend.mobile_spend==0 & member_spend.desktop_spend>0], ‘channel’] = ‘desktop’
member_spend[member_spend.mobile_spend>0 & member_spend.desktop_spend>0], ‘channel’] = ‘both’
tot_members = member_spend.groupby([‘date’, ‘channel’]).size().to_frame(‘tot_members’).reset_index()
tot_spend = member_spend.groupby([‘date’, ‘channel’].agg({‘mobile_spend’:sum, ‘desktop_spend’:sum}).to_frame([‘mobile_spend’, ‘desktop_spend’])
tot_spend[‘tot_spend’] = tot_spend[‘mobile_spend’] + tot_spend[‘desktop_spend’]
output = tot_members.concat(tot_spend[‘tot_spend’])
*/

----------------------------------------------------
/*
Problem: table emp_history
member_id|company_name|year_start 
1): count members who ever moved from Microsoft to Google? .
output:
counts
5
2): count members who directly moved from Microsoft to Google? 
output:
counts
3
*/

/*
Q1:*/
SELECT a.COUNT(DISTINCT member_id)
FROM emp_history a
JOIN emp_history b
WHERE a.member_id = b.member_id 
AND a.year_start < b.year_start 
AND a.company_name = 'Microsoft'
AND b.company_name = 'Google'
;
/*
Q2:
(Microsoft - Linkedin - Google doesn't count)
 1) SQL solution: (assumption: no end date. define move
from company A to company B if the start date of company B is after the
start date of company A, Microsoft - Linkedin - Google )
*/
SELECT COUNT(DISTINCT member_id)
FROM (
    SELECT member_id, company_name,
    LEAD(company_name) OVER (PARTITION BY member_id ORDER BY year_start) AS nxt_company_name
    FROM emp_history
) AS t
WHERE t.company_name = 'Microsoft' AND t.nxt_company_name = 'Google'
;

-- Python pandas:
/*
table[‘next_company’] = table.sort_values(by=[‘member_id’, ‘year_start’]).groupby([‘member_id’])[‘company_name’].shift(1)
table[(table.company_name == ‘Microsoft’) & (table.next_company == ‘Google’)][‘member_id’].unique()
*/

-----------------------------------------
/*
The input spending table is
member_id    date    channel   spend
1001    1/1/2018    mobile    100
1001    1/1/2018    desktop    100
1002    1/1/2018    mobile    100
1002    1/2/2018    mobile    100
1003    1/1/2018    desktop    100
1003    1/2/2018    desktop    100

The output data is
date    channel    total_spend    total_members
1/1/2018    desktop    100    1
1/1/2018    mobile    100    1
1/1/2018    both    200    1
1/2/2018    desktop    100    1
1/2/2018    mobile    100    1
*/ /*
Q1:
Problem:  Member can make purchase via either mobile  or desktop platform.
Using the data table to determine the total number of member and revenue
for mobile-only, desktop_only and mobile_desktop.
*/ -- SQL
WITH member_spend AS
    (SELECT date, member_id, SUM(CASE
                                    WHEN channel = ‘mobile’ THEN spend
                                    ELSE 0
                                END) AS mobile_spend, 
                             SUM(CASE
                                    WHEN channel = ‘desktop’ THEN spend
                                    ELSE 0
                                END) AS desktop_spend
     FROM spending
     GROUP BY date, member_id)
SELECT date, CASE
                 WHEN mobile_spend > 0
                      AND desktop_spend = 0 THEN ‘mobile’
                 WHEN mobile_spend = 0
                      AND desktop_spend > 0 THEN ‘desktop’
                 WHEN mobile_spend > 0
                      AND desktop_spend > 0 THEN ‘both’
             END AS channel,
             SUM(mobile_spend + desktop_spend) AS total_spend,
             COUNT(*) AS total_members
FROM member_spend
GROUP BY date, CASE
                   WHEN mobile_spend > 0
                        AND desktop_spend = 0 THEN ‘mobile’
                   WHEN mobile_spend = 0
                        AND desktop_spend > 0 THEN ‘desktop’
                   WHEN mobile_spend > 0
                        AND desktop_spend > 0 THEN ‘both’
               END ;


