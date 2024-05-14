from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    # 学生表，包含学生id（主键）和姓名
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    # 通过relationship()方法，将Student模型与Course模型关联起来（不会在数据库中生成额外的内容）
    courses = db.relationship('Course', secondary='grade', backref=db.backref('students', lazy=True))