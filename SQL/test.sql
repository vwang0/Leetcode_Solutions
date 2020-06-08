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