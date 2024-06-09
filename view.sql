CREATE VIEW StudentCourseScores AS
SELECT student.student_name AS student_name, 
       course.course_name AS course_name, 
       enrollment.score AS score
FROM enrollment
JOIN student ON student.student_id = enrollment.student_id
JOIN course ON course.course_id = enrollment.course_id;