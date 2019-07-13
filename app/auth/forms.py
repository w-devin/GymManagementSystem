from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, RadioField , BooleanField, IntegerField , SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Regexp, EqualTo
from wtforms import ValidationError
from ..models import Role


class LoginForm(FlaskForm):
    phone = StringField('Phone', validators=[DataRequired(), Length(1, 11)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me Logged in')
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    phone = StringField(label='Phone', validators=[DataRequired(), Length(1, 11)])
    name = StringField(label='Name', validators=[DataRequired(), Length(1, 64)])
    age = IntegerField(label='Age', validators=[DataRequired()])
    gender = RadioField(label='Gender', choices=[(True, '男'), (False, '女')], validators=[DataRequired()])

    identify = SelectField(label='identify', choices=[('admin', '管理员'), ('vip', '会员'), ('staff', '工作人员'), ('coach', '教练'), ('cleaners', '保洁人员')])
    reserved = SelectField(label='VIP level', choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')])

    password = PasswordField(label='Password', validators=[DataRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField(label='Confirm password', validators=[DataRequired()])

    submit = SubmitField(label='Register')

    def validate_phone(self, field):
        if Role.query.filter_by(phone=field.data).first():
            raise ValidationError('Phone already registered')
