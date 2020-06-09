
SELECT user_id,
       IFNULL(unix_timestamp - prev_time, -1) AS delta_time
FROM        
    (SELECT user_id, unix_timestamp, 
    LEAD(unix_timestamp) OVER (PARTITION BY user_id ORDER BY unix_timestampe DESC) AS prev_time, 
    ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY unix_timestamp DESC) AS ord_desc
    FROM query_one) AS tmp
WHERE ord_desc = 1 
OEDER BY user_id 
;

SELECT count(distinct member_id) as counts
FROM emp_history a
Left join emp_history b ON a.member_id=b.member_id
WHERE a.company_name=’Microsoft’
    and b.company_name=’Google’
    and b.year_start> a.year_start

====================================Q2
SELECT IFNULL(100*SUM(CASE
                          WHEN m.user_id IS NULL THEN 1
                          ELSE 0 END)/COUNT(*), 0) AS WEB_ONLY,
       IFNULL(100*SUM(CASE
                          WHEN w.user_id IS NULL THEN 1
                          ELSE 0 END)/COUNT(*), 0) AS MOBILE_ONLY,
       IFNULL(100*SUM(CASE
                          WHEN w.user_id IS NOT NULL
                               AND m.user_id IS NOT NULL THEN 1
                          ELSE 0 END)/COUNT(*), 0) AS BOTH
FROM
    (SELECT DISTINCT user_id
    FROM data_web) AS w
FULL OUTER JOIN
    (SELECT DISTINCT user_id
     FROM data_mobile) AS m 
ON w.user_id = m.user_id

WITH temp AS
    (SELECT DISTINCT user_id,
                     page AS p1
     FROM data_web) AS w
FULL OUTER JOIN
    (SELECT DISTINCT user_id,
                     page AS p2
     FROM data_mobile) AS m ON w.user_id = m.user_id )
SELECT IFNULL(SUM(IF(p1 IS NULL,1,0))/COUNT(*),0)*100 AS MOBILE_ONLY,
       IFNULL(SUM(IF(p2 IS NULL,1,0))/COUNT(*),0)*100 AS WEB_ONLY,
       IFNULL(SUM(CASE
                      WHEN p1 is not null
                           AND p2 is not null THEN 1
                      ELSE 0
                  END)/COUNT(*),0)*100 AS both
FROM temp

WITH temp AS
    (SELECT use_id,
            unix_timestamp,
            LEAD(unix_timestamp) OVER (PARTITION BY user_id
                                       ORDER BY unix_stamps DESC) AS prev_time,
                                      ROW_NUMBER() OVER (PARTITION BY user_id
                                                         ORDER BY unix_stamps DESC) AS ord_num
     FROM query_one)
SELECT user_id,
       IFNULL(unix_timestamp-pre_time, -1) as delta_time
FROM temp
WHERE ord_num=1
ORDER BY user_id

SELECT Stu.student_id,
    Stu.student_name,
    Sub.subject_name,
    COUNT(Exam.subject_name) as attended_exams
FROM Students AS Stu
JOIN Subjects AS Sub
LEFT JOIN Examinations AS Exam 
ON Stu.student_id = Exam.student_id
AND Sub.subject_name = Exam.subject_name
GROUP BY Stu.student_id, Sub.subject_name
ORDER BY student_id, subject_name
;



SELECT
S1.sub_id AS post_id,
COUNT(DISTINCT S2.sub_id) AS number_of_comments
FROM Submissions S1
LEFT JOIN Submissions S2
ON S1.sub_id = S2.parent_id
WHERE S1.parent_id IS NULL
GROUP BY S1.sub_id
;

SELECT COUNT(DISTINCT member_id)
FROM
    (SELECT member_id,
            company_name,
            LEAD(compnay_name) OVER (PATITION BY member_id
                                     ORDER by year_start) AS nxt_comp_name
     FROM emp_history) AS t
WHERE t.company_name =’Microsoft’
    AND nxt_comp_name =’GOOGLE’

    WITH member_spend AS
    (SELECT date, member_id,
                  SUM(CASE
                          WHEN channel=’mobile’ THEN spend
                          ELSE 0
                      END) mob_spend,
                  SUM(CASE
                          WHEN channel=’desktop’ THEN spend
                          ELSE 0
                      END) desk_spend
     FROM spending
     GROUP BY date, member_id)
SELECT date, CASE
                 WHEN mob_spend >0
                      AND desk_top=0 THEN ‘mobile’
                 WHEN mob_spend =0
                      AND desk_top>0 THEN ‘desktop’
                 WHEN mob_spend >0
                      AND desk_top>0 THEN ‘both’
             END AS platform,
             mob_spend+desk_spend AS total_spend,
             COUNT(*) AS total_members
FROM member_spend
GROUP BY date, platform