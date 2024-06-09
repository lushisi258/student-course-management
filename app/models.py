from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    student_id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(120), nullable=False)
    register_date = db.Column(db.Date, nullable=False)

class Course(db.Model):
    course_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(120), nullable=False)
    teacher = db.Column(db.String(120), nullable=False)

class Enrollment(db.Model):
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), primary_key=True)
    score = db.Column(db.Float, nullable=True)

# 视图
class StudentCourseScores(db.Model):
    __tablename__ = 'StudentCourseScores'
    student_name = db.Column(db.String(120), primary_key=True)
    course_name = db.Column(db.String(120), primary_key=True)
    score = db.Column(db.Float)