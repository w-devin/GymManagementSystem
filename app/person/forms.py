from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, RadioField, BooleanField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

import sys



class ModifyForm(FlaskForm):
    phone = StringField(label='Phone', validators=[DataRequired()], render_kw={'readonly':True})
    name = StringField(label='Name', validators=[DataRequired('name')])
    age = IntegerField(label='Age', validators=[DataRequired('age')])

    gender = RadioField(label='Gender', choices=[('1', '男'), ('0', '女')], validators=[DataRequired('gender')])

    identify = SelectField(label='identify',
                           choices=[('admin', '管理员'), ('vip', '会员'), ('staff', '工作人员'),
                                    ('coach', '教练'), ('cleaners', '保洁人员')],
                           validators=[DataRequired('identify')])

    reserved = SelectField(label='VIP level',
                           choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')],
                           validators=[DataRequired()])

    password = PasswordField(label='Password',
                             validators=[DataRequired('password'), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField(label='Confirm password', validators=[DataRequired('password2')])

    submit = SubmitField(label='Modify')
