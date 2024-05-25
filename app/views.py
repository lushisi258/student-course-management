from flask import Blueprint, render_template

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