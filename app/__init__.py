import os
from flask import Flask
from .views import views
from .models import db
import pymysql
pymysql.install_as_MySQLdb()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:25858.asd@localhost/scmdb'
    db.init_app(app)

    app.register_blueprint(views)

    return app