from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])     # 可选参数validators用于验证输入字段是否符合预期
    password = PasswordField('Password', validators=[DataRequired()])   # DataRequired()要求非空，处理无效表单输入的方式是重新显示表单
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])     # 可选参数validators用于验证输入字段是否符合预期
    password = PasswordField('Password', validators=[DataRequired()])   # DataRequired()要求非空，处理无效表单输入的方式是重新显示表单
    submit = SubmitField('Sign Up')
