DELIMITER $$

CREATE TRIGGER check_student_id_before_insert
BEFORE INSERT ON student
FOR EACH ROW
BEGIN
    IF LENGTH(NEW.student_id) > 5 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'make student_id length less than 5';
    END IF;
END$$

DELIMITER ;