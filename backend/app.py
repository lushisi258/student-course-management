from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 创建Flask应用
app = Flask(__name__)

# 读取数据库密码
with open('password.txt', 'r') as f:
    password = f.read().strip()

# 配置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:' + password + '@localhost/scmdb'

# 创建数据库对象    
db = SQLAlchemy(app)

# 导入views
from views.course_view import *
from views.student_view import *
from views.grade_view import *