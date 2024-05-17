from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# 创建课程表单，用于录入新的课程信息
class CourseForm(FlaskForm):
    name = StringField('Course Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

# 创建学生表单，用于录入新的学生信息
class StudentForm(FlaskForm):
    name = StringField('Student Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

# 创建成绩表单，用于录入新的成绩信息
class ScoreForm(FlaskForm):
    student_id = StringField('Student ID', validators=[DataRequired()])
    course_id = StringField('Course ID', validators=[DataRequired()])
    score = StringField('Score', validators=[DataRequired()])
    submit = SubmitField('Submit')