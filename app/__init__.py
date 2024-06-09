from flask import Flask
from .views import views
from .models import db
from config import password

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:{password}@localhost/scmdb'
    db.init_app(app)

    app.register_blueprint(views)

    return app