# Write your MySQL query statement below
SELECT stu.student_id, stu.student_name, subj.subject_name, COUNT(exam.student_id) attended_exams
FROM Students stu
CROSS JOIN Subjects subj
LEFT JOIN Examinations exam on stu.student_id = exam.student_id and subj.subject_name = exam.subject_name
GROUP BY stu.student_id, stu.student_name, subj.subject_name
ORDER BY stu.student_id, subj.subject_name