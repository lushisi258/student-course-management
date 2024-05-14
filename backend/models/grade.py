from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Grade(db.Model):
    # 成绩表，包含学生id（student的外键），课程id（course的外键）和成绩
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), primary_key=True)
    grade = db.Column(db.Integer)
    # 通过relationship()方法，将Grade模型与Student和Course模型关联起来（不会在数据库中生成额外的内容）
    student = db.relationship('Student', backref=db.backref('grades', lazy=True))
    course = db.relationship('Course', backref=db.backref('grades', lazy=True))