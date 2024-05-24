import sqlalchemy
from models.student import Student
from forms.forms import StudentForm
from flask import render_template, abort, redirect, url_for
from app import app, db
from flask import request

# 获取所有的学生信息
@app.route('/students')
def get_students():
    students = Student.query.all()
    return render_template('students.html', students=students)

# 获取某个学生的具体信息
@app.route('/student/<int:student_id>')
def get_student(student_id):
    student = Student.query.get(student_id)
    if student is None:
        abort(404)
    return render_template('student.html', student=student)

# 录入新的学生信息
@app.route('/student/new', methods=['GET', 'POST'])
def new_student():
    data = request.get_json()

    # 创建表单对象
    form = StudentForm()

    # 从 JSON 数据中填充表单字段
    form.id.data = data.get('id')
    form.name.data = data.get('name')
    form.register_year.data = data.get('register_year')

    # 验证表单数据
    if form.validate():
        # 创建新的学生对象
        student = Student(name=form.name.data, register_year=form.register_year.data)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('new_student.html', student_id=student.id))
    return render_template('unsucced_new.html', form=data)

# 修改某个学生的信息
@app.route('/student/<int:student_id>/edit', methods=['POST'])
def edit_student(student_id):
    student = Student.query.get(student_id)
    if student is None:
        abort(404)
    form = StudentForm(obj=student)
    if form.validate_on_submit():
        form.populate_obj(student)
        db.session.commit()
        return redirect(url_for('get_student', student_id=student.id))
    return render_template('edit_student.html', form=form)

# 删除某个学生的信息
@app.route('/student/<int:student_id>/delete', methods=['POST'])
def delete_student(student_id):
    student = Student.query.get(student_id)
    if student is None:
        abort(404)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('get_students'))
