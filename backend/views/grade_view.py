from models.grade import Grade
from forms.forms import GradeForm
from flask import render_template, abort, redirect, url_for
from app import app, db

# 录入成绩
@app.route('/grade/new', methods=['GET', 'POST'])
def new_grade():
    form = GradeForm()
    if form.validate_on_submit():
        grade = Grade(student_id=form.student_id.data, course_id=form.course_id.data, score=form.score.data)
        db.session.add(grade)
        db.session.commit()
        return redirect(url_for('get_grade', grade_id=grade.id))
    return render_template('new_grade.html', form=form)

# 修改成绩
@app.route('/grade/<int:grade_id>/edit', methods=['GET', 'POST'])
def edit_grade(grade_id):
    grade = Grade.query.get(grade_id)
    if grade is None:
        abort(404)
    form = GradeForm(obj=grade)
    if form.validate_on_submit():
        form.populate_obj(grade)
        db.session.commit()
        return redirect(url_for('get_grade', grade_id=grade.id))
    return render_template('edit_grade.html', form=form)

# 删除成绩
@app.route('/grade/<int:grade_id>/delete', methods=['POST'])
def delete_grade(grade_id):
    grade = Grade.query.get(grade_id)
    if grade is None:
        abort(404)
    db.session.delete(grade)
    db.session.commit()
    return redirect(url_for('get_grades'))

# 查询某个成绩
@app.route('/grade/<int:grade_id>')
def get_grade(grade_id):
    grade = Grade.query.get(grade_id)
    if grade is None:
        abort(404)
    return render_template('grade.html', grade=grade)

