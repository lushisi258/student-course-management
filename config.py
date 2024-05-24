import os

SECRET_KEY = os.urandom(24)
SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'