from flask import Blueprint, render_template, request
from pymysql.err import OperationalError
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy import text
from .models import db, Student, Course, Enrollment, StudentCourseScores

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
    except Exception as e:
        db.session.rollback()
        result = '添加失败: 出现错误'
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
    # 调用存储过程
    sql = text("CALL UpdateStudentInfo(:student_id, :student_name, :register_date)")
    result = db.session.execute(sql, {'student_id': student_id, 'student_name': student_name, 'register_date': register_date}).fetchone()
    # 检查存储过程的返回结果
    if result[0] == 'cannot update student info with empty student name':
        # 如果学生姓名为空，则不提交事务，并返回错误消息
        db.session.rollback()
    else:
        # 如果没有错误，提交事务
        db.session.commit()
    return render_template('update/update_student.html', result=result[0])

# 跳转到删除学生页面
@views.route('/turn_to_delete_student')
def turn_to_delete_student():
    return render_template('/delete/delete_student.html')
@views.route('/delete_student', methods=['POST'])
def delete_student():
    student_id = request.form.get('student_id')
    try:
        # 开始事务
        db.session.begin()
        # 删除该学生的所有选课记录
        Enrollment.query.filter_by(student_id=student_id).delete()
        # 删除学生记录
        student = Student.query.get(student_id)
        if student:
            db.session.delete(student)
        # 提交事务
        db.session.commit()
        result = "成功删除学生信息"
    except SQLAlchemyError as e:
        # 如果出现错误，回滚事务
        db.session.rollback()
        result = "出错了 :( " + str(e)
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
    result = '课程信息不存在'
    course_id = request.form.get('course_id')
    course = Course.query.filter_by(course_id=course_id).first()
    if course:
        db.session.delete(course)
        db.session.commit()
        result = '课程删除成功'
        print('课程删除成功')
    return render_template('/delete/delete_course.html', result=result)

# 跳转到查询课程页面
@views.route('/turn_to_query_course')
def turn_to_query_course():
    return render_template('/query/query_course.html')
@views.route('/query_course', methods=['POST'])
def query_course():
    result = '查询成功'
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
    if not courses:
        result = '查询失败，当前信息有误'
        return render_template('/query/query_course.html', result=result)
    return render_template('/query/query_course.html', result=result, courses=courses)


'''
有关选课的路由
'''
@views.route('/enrollment')
def enrollment():
    return render_template('/base/enrollment.html')
# 跳转到选课页面
@views.route('/turn_to_add_enrollment')
def turn_to_add_enrollment():
    return render_template('/add/add_enrollment.html')
@views.route('/add_enrollment', methods=['POST'])
def add_enrollment():
    student_id = request.form.get('student_id')
    course_id = request.form.get('course_id')
    student = Student.query.filter_by(student_id=student_id).first()
    course = Course.query.filter_by(course_id=course_id).first()
    if student and course:
        student.courses.append(course)
        db.session.commit()
        result = '选课成功'
    else:
        result = '选课失败，当前信息有误'
    return render_template('/enrollment/enrollment.html', result=result)

# 跳转到退课页面
@views.route('/turn_to_delete_enrollment')
def turn_to_delete_enrollment():
    return render_template('/delete/delete_enrollment.html')
@views.route('/delete_enrollment', methods=['POST'])
def delete_enrollment():
    student_id = request.form.get('student_id')
    course_id = request.form.get('course_id')
    student = Student.query.filter_by(student_id=student_id).first()
    course = Course.query.filter_by(course_id=course_id).first()
    if student and course:
        student.courses.remove(course)
        db.session.commit()
        result = '退课成功'
    else:
        result = '退课失败，当前信息有误'
    return render_template('/enrollment/delete_enrollment.html', result=result)

# 跳转到查询选课页面
@views.route('/turn_to_query_enrollment')
def turn_to_query_enrollment():
    return render_template('/query/query_enrollment.html')
@views.route('/query_enrollment', methods=['POST'])
def query_enrollment():
    student_id = request.form.get('student_id')
    course_id = request.form.get('course_id')
    # 初始化结果
    courses = []
    students = []
    enrollments = []
    scores = []
    result = '查询成功'
    if student_id and course_id:
        enrollments = Enrollment.query.filter_by(student_id=student_id, course_id=course_id).all()
    elif student_id:
        course_ids = Enrollment.query.filter_by(student_id=student_id).all()
        for course_id in course_ids:
            courses.append(Course.query.filter_by(course_id=course_id.course_id).first())
    elif course_id:
        student_ids = Enrollment.query.filter_by(course_id=course_id).all()
        for student_id in student_ids:
            students.append(Student.query.filter_by(student_id=student_id.student_id).first())
    else:
        scores = StudentCourseScores.query.all()
    if (not courses) and (not students) and (not enrollments) and (not scores):
        result = '查询失败，当前信息有误'
    return render_template('/query/query_enrollment.html', result=result, courses=courses, students=students, enrollments=enrollments, scores = scores)