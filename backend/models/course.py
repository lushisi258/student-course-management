from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Course(db.Model):
    # 课程表，包含课程id（主键），课程名和教师名
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    teacher = db.Column(db.String(100), nullable=False)