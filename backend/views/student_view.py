from models.student import Student
from forms.forms import StudentForm
from flask import render_template, abort, redirect, url_for
from app import app, db

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
    form = StudentForm()
    if form.validate_on_submit():
        student = Student(name=form.name.data, age=form.age.data)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('get_student', student_id=student.id))
    return render_template('new_student.html', form=form)

# 修改某个学生的信息
@app.route('/student/<int:student_id>/edit', methods=['GET', 'POST'])
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

