from flask import Blueprint, render_template
from sqlalchemy.exc import IntegrityError
from flask import request
from .models import db, Student, Course

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('/base/index.html')

''' 
有关学生的路由
'''
# 跳转到学生管理页面
@views.route('/student')
def student():
    return render_template('/base/student.html')
# 跳转到添加学生页面
@views.route('/turn_to_add_student')
def turn_to_add_student():
    return render_template('/add/add_student.html')
@views.route('/add_student', methods=['POST'])
def add_student():
    try:
        student_id = request.form.get('student_id')
        student_name = request.form.get('student_name')
        register_date = request.form.get('register_date')
        new_student = Student(student_id=student_id, student_name=student_name, register_date=register_date)
        db.session.add(new_student)
        db.session.commit()
        result = '学生添加成功'
    except IntegrityError:
        db.session.rollback()
        result = '添加失败，学生信息已存在'
    return render_template('/add/add_student.html', result=result)

# 跳转到修改学生页面
@views.route('/turn_to_update_student')
def turn_to_update_student():
    return render_template('/update/update_student.html')
@views.route('/update_student', methods=['POST'])
def update_student():
    student_id = request.form.get('student_id')
    student_name = request.form.get('student_name')
    register_date = request.form.get('register_date')
    student = Student.query.filter_by(student_id=student_id).first()
    if student:
        student.student_name = student_name
        student.register_date = register_date
        db.session.commit()
        result='学生信息修改成功'
    else:
        result='学生信息不存在'
    return render_template('update/update_student.html', result=result)

# 跳转到删除学生页面
@views.route('/turn_to_delete_student')
def turn_to_delete_student():
    return render_template('/delete/delete_student.html')
@views.route('/delete_student', methods=['POST'])
def delete_student():
    student_id = request.form.get('student_id')
    student = Student.query.filter_by(student_id=student_id).first()
    if student:
        db.session.delete(student)
        db.session.commit()
        result = '学生删除成功'
    else:
        result = '学生信息不存在'
    return render_template('/delete/delete_student.html', result=result)

# 跳转到查询学生页面
@views.route('/turn_to_query_student')
def turn_to_query_student():
    return render_template('/query/query_student.html')
@views.route('/query_student', methods=['POST'])
def query_student():
    if request.form.get('student_id'):
        student_id = request.form.get('student_id')
        students = Student.query.filter_by(student_id=student_id).all()
    elif request.form.get('student_name'):
        student_name = request.form.get('student_name')
        students = Student.query.filter_by(student_name=student_name).all()
    elif request.form.get('register_date'):
        register_date = request.form.get('register_date')
        students = Student.query.filter_by(register_date=register_date).all()
    else:
        students = Student.query.all()
    return render_template('/query/query_student.html', students=students)


'''
有关课程的路由
'''
@views.route('/course')
def course():
    return render_template('/base/course.html')
# 跳转到添加课程页面
@views.route('/turn_to_add_course')
def turn_to_add_course():
    return render_template('/add/add_course.html')
@views.route('/add_course', methods=['POST'])
def add_course():
    try:
        course_id = request.form.get('course_id')
        course_name = request.form.get('course_name')
        teacher = request.form.get('course_teacher')
        course = Course(course_id=course_id, course_name=course_name, teacher=teacher)
        db.session.add(course)
        db.session.commit()
        result = '课程添加成功'
    except IntegrityError:
        db.session.rollback()
        result = '添加失败，课程信息已存在'
    return render_template('/add/add_course.html', result=result)

# 跳转到修改课程页面
@views.route('/turn_to_update_course')
def turn_to_update_course():
    return render_template('/update/update_course.html')
@views.route('/update_course', methods=['POST'])
def update_course():
    course_id = request.form.get('course_id')
    course_name = request.form.get('course_name')
    course_teacher = request.form.get('course_teacher')
    course = Course.query.filter_by(course_id=course_id).first()
    if course:
        course.course_name = course_name
        course.teacher = course_teacher
        db.session.commit()
        result='课程信息修改成功'
    else:
        result='课程信息不存在'
    return render_template('update/update_course.html', result=result)

# 跳转到删除课程页面
@views.route('/turn_to_delete_course')
def turn_to_delete_course():
    return render_template('/delete/delete_course.html')
@views.route('/delete_course', methods=['POST'])
def delete_course():
    course_id = request.form.get('course_id')
    course = Course.query.filter_by(course_id=course_id).first()
    if course:
        db.session.delete(course)
        db.session.commit()
        result = '课程删除成功'
    else:
        result = '课程信息不存在'
    return render_template('/delete/delete_course.html', result=result)

# 跳转到查询课程页面
@views.route('/turn_to_query_course')
def turn_to_query_course():
    return render_template('/query/query_course.html')
@views.route('/query_course', methods=['POST'])
def query_course():
    if request.form.get('course_id'):
        course_id = request.form.get('course_id')
        courses = Course.query.filter_by(course_id=course_id).all()
    elif request.form.get('course_name'):
        course_name = request.form.get('course_name')
        courses = Course.query.filter_by(course_name=course_name).all()
    elif request.form.get('course_teacher'):
        teacher = request.form.get('course_teacher')
        courses = Course.query.filter_by(teacher=teacher).all()
    else:
        courses = Course.query.all()
    return render_template('/query/query_course.html', courses=courses)
