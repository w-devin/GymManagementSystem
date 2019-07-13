import os
from app.models import Role
from flask_login import UserMixin
from app import db, login_manager
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'Test.sqlite')
db.init_app(app)


class TT(UserMixin, db.Model):
    __tablename__ = 'test'
    id = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(64))

t = TT(name='ting', id=1)
