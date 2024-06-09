DELIMITER //
CREATE PROCEDURE UpdateStudentInfo(IN p_student_id INT, IN p_student_name VARCHAR(120), IN p_register_date DATE)
BEGIN
    IF p_student_name IS NOT NULL AND TRIM(p_student_name) <> '' THEN
        IF EXISTS (SELECT 1 FROM student WHERE student_id = p_student_id) THEN
            UPDATE student
            SET student_name = p_student_name, register_date = p_register_date
            WHERE student_id = p_student_id;
            SELECT 'updated' AS result;
        ELSE
            SELECT 'no student info' AS result;
        END IF;
    ELSE
        SELECT 'cannot update student info with empty student name' AS result;
    END IF;
END //
DELIMITER ;