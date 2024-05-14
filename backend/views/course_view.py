from models.course import Course
from forms.forms import CourseForm
from flask import render_template, abort, redirect, url_for
from app import app, db

# 获取所有的课程
@app.route('/courses')
def get_courses():
    courses = Course.query.all()
    return render_template('courses.html', courses=courses)

# 获取某个课程的具体信息
@app.route('/course/<int:course_id>')
def get_course(course_id):
    course = Course.query.get(course_id)
    if course is None:
        abort(404)
    return render_template('course.html', course=course)

# 录入新的课程信息
@app.route('/course/new', methods=['GET', 'POST'])
def new_course():
    form = CourseForm()
    if form.validate_on_submit():
        course = Course(name=form.name.data)
        db.session.add(course)
        db.session.commit()
        return redirect(url_for('get_course', course_id=course.id))
    return render_template('new_course.html', form=form)

# 修改某个课程的信息
@app.route('/course/<int:course_id>/edit', methods=['GET', 'POST'])
def edit_course(course_id):
    course = Course.query.get(course_id)
    if course is None:
        abort(404)
    form = CourseForm(obj=course)
    if form.validate_on_submit():
        form.populate_obj(course)
        db.session.commit()
        return redirect(url_for('get_course', course_id=course.id))
    return render_template('edit_course.html', form=form)

# 删除某个课程
@app.route('/course/<int:course_id>/delete', methods=['POST'])
def delete_course(course_id):
    course = Course.query.get(course_id)
    if course is None:
        abort(404)
    db.session.delete(course)
    db.session.commit()
    return redirect(url_for('get_courses'))