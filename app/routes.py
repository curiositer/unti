# from app import app
#
#
# @app.route('/')
# @app.route('/index')
# def index():
#     user = {'username': 'Miguel'}
#     return '''
# <html>
#     <head>
#         <title>Home Page - Microblog</title>
#     </head>
#     <body>
#         <h1>Hello, ''' + user['username'] + '''!</h1>
#         <input type="text" /> <!-- This is for text input -->
#         <input type="file" /> <!-- This is for uploading files -->
#         <input type="checkbox" /> <!-- This is for checkboxes -->
#     </body>
# </html>'''

from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm
from flask_wtf.csrf import CsrfProtect
from app.models import User
from flask_login import login_user, login_required
from flask_login import LoginManager, current_user
from flask_login import logout_user


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/test')
def test():
    res = 'The method of your request is [%s], and your arguments are %s'
    return res % (request.method, request.args)


@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)      # 采用index.html的模板

# use login manager to manage session
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'
login_manager.init_app(app=app)

# 这个callback函数用于reload User object，根据session中存储的user id
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

# csrf protection
csrf = CsrfProtect()
csrf.init_app(app)


@app.route('/login', methods=['GET', 'POST'])   # 设置允许post提交方式
def login():
    form = LoginForm()
    if form.validate_on_submit():   # 执行form校验，get请求返回false会使得跳过if
        # flash('Login requested for user {}, remember_me={}'.format(     # flash()函数是向用户显示消息的有效途径
        #     form.username.data, form.remember_me.data))
        user_name = form.username
        password = form.password
        remember_me = form.remember_me
        user = User(user_name)
        if user.verify_password(password):
            login_user(user, remember=remember_me)
            return redirect(request.args.get('next') or url_for('main'))
        else:
            flash('Login requested for user {}, remember_me={}'.format(     # flash()函数是向用户显示消息的有效途径
                form.username.data, form.remember_me.data))
        # return redirect(url_for('index'))       # 重定向到它的参数所关联的URL
    return render_template('login.html', title='Sign In', form=form)


@app.route('/signup')
def signup():
    form = LoginForm()
    if form.validate_on_submit():  # 执行form校验，get请求返回false会使得跳过if
        # flash('Login requested for user {}, remember_me={}'.format(     # flash()函数是向用户显示消息的有效途径
        #     form.username.data, form.remember_me.data))
        user_name = form.username
        password = form.password
# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#
