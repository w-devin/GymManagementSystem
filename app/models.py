from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flask_login import UserMixin
from . import db, login_manager


class Role(UserMixin, db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    phone = db.Column(db.Integer, unique=True)
    age = db.Column(db.Integer)
    gender = db.Column(db.Boolean)
    identify = db.Column(db.String(64))
    reserved = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<Role %r>' % self.name

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        print('asfds')
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(user_id):
    return Role.query.get(int(user_id))
