from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, RadioField , BooleanField, IntegerField , SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

import sys


class LoginForm(FlaskForm):
    phone = StringField('手机号', validators=[DataRequired(), Length(1, 11)])
    password = PasswordField('密码', validators=[DataRequired()])
    remember_me = BooleanField('保持登录')
    submit = SubmitField('登录')


class RegistrationForm(FlaskForm):
    phone = StringField(label='Phone', validators=[DataRequired()])
    name = StringField(label='Name', validators=[DataRequired()])
    age = IntegerField(label='Age', validators=[DataRequired()])

    gender = RadioField(label='Gender', choices=[('1', '男'), ('0', '女')], validators=[DataRequired()])

    identify = SelectField(label='identify',
                           choices=[('admin', '管理员'), ('vip', '会员'), ('staff', '工作人员'),
                                    ('coach', '教练'), ('cleaners', '保洁人员')],
                           validators=[DataRequired()])
    reserved = SelectField(label='VIP level',
                           choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')],
                           validators=[DataRequired()])

    password = PasswordField(label='Password',
                             validators=[DataRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField(label='Confirm password', validators=[DataRequired()])

    submit = SubmitField(label='Register')

    def validate_phone(self, field):
        if User.query.filter_by(phone=field.data).first():
            raise ValidationError('Phone already registered')
