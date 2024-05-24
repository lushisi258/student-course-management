from models.score import Score
from forms.forms import ScoreForm
from flask import render_template, abort, redirect, url_for
from app import app, db

# 录入成绩
@app.route('/score/new', methods=['GET', 'POST'])
def new_score():
    form = ScoreForm()
    if form.validate_on_submit():
        score = Score(student_id=form.student_id.data, course_id=form.course_id.data, score=form.score.data)
        db.session.add(score)
        db.session.commit()
        return redirect(url_for('get_score', score_id=score.id))
    return render_template('new_score.html', form=form)

# 修改成绩
@app.route('/score/<int:score_id>/edit', methods=['GET', 'POST'])
def edit_score(score_id):
    score = Score.query.get(score_id)
    if score is None:
        abort(404)
    form = ScoreForm(obj=score)
    if form.validate_on_submit():
        form.populate_obj(score)
        db.session.commit()
        return redirect(url_for('get_score', score_id=score.id))
    return render_template('edit_score.html', form=form)

# 删除成绩
@app.route('/score/<int:score_id>/delete', methods=['POST'])
def delete_score(score_id):
    score = Score.query.get(score_id)
    if score is None:
        abort(404)
    db.session.delete(score)
    db.session.commit()
    return redirect(url_for('get_scores'))

# 查询某个成绩
@app.route('/score/<int:score_id>')
def get_score(score_id):
    score = Score.query.get(score_id)
    if score is None:
        abort(404)
    return render_template('score.html', score=score)

