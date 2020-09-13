/*

SQL 2 and  Python 1
被要求分别用SQL和Python做一遍这道题目. check 1point3acres for more.
原始数据如下，status如果是repair就是刚送修，如果是online就是修好了。
server_id	repair_status	as_of_date
1	repair	2020-01-01
1	online	2020-01-08
2	repair	2020-01-05
2	online	2020-01-11
3	repair	2020-01-10
3	online	2020-01-22
4	repair	2020-02-02
4	online	2020-02-04
4	repair	2020-02-10
4	online	2020-02-16
5	repair	2020-03-01

要求整理出来每个server的修理时间。
server4被修理两次，需要把两次时间加起来
server5至今没有online，于是用今天的日期当作online date计算迄今为止的修理时长
结果应该长这样
server_id	repair_days
1	7
2	6
3	12
4	8
5	Today - '2020-03-01'
*/
with temp as
    (SELECT server_id,
            repair_status,
            as_of_date,
            LEAD(as_of_date, 1) OVER (PARTITION BY server_id ORDER BY as_of_date) next_date
     FROM table)

SELECT server_id,
       SUM(IFNULL(DATE_DIFF(next_date, as_of_date), CURDATE()- as_of_date)) repair_days
from temp
where repair_status= 'repair'
group by 1;

-- Solution 2
with temp as
(select server_id, repair_status, as_of_date
, lead(repair_status, 1) over (partition by server_id order by as_of_date) next_status
, lead(as_of_date, 1) over (partition by server_id order by as_of_date) next_date
from table
)

select server_id
,sum(case when next_status= 'online' then date_diff('day', as_of_date, next_date)
      when next_date is null then date_diff('day', as_of_date, current_date) end) repair_days
from temp
where repair_status= 'repair'
group by 1
;

/*
``` Pandas
import pandas as pd
data = pd.read_csv('status.csv')
data['as_of_date'] = pd.to_datetime(data['as_of_date'])
data['lead_date'] = data.groupby('server_id')['as_of_date'].shift(-1)
data['lead_status'] = data.groupby('server_id')['repair_status'].shift(-1)
data = data.loc[data['repair_status']=='repair']
data['lead_date'] = pd.to_datetime(data['lead_date'].fillna(pd.to_datetime("today")))
data['repair_days'] =  (data['lead_date'] - data['as_of_date']).dt.days
data.groupby('server_id')['repair_days'].sum()
```
*/