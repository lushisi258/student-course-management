import os
from flask import Flask
from .views import views
from .models import db
from config import password
import pymysql
pymysql.install_as_MySQLdb()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:'+password+'@localhost/scmdb'
    db.init_app(app)

    app.register_blueprint(views)

    return app