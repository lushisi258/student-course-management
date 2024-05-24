from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import json

# 读取 JSON 文件
with open('backend/config.json', 'r') as f:
    config = json.load(f)

# 读取数据库密码
password = config['password']

# 创建Flask应用
app = Flask(__name__)

# 配置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:' + password + '@localhost/scmdb'


# 创建数据库对象    
db = SQLAlchemy(app)

# 导入views
from views.course_view import *
from views.student_view import *
from views.score_view import *

if __name__ == "__main__":
    app.run(debug=True)