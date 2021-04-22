from flask_login import LoginManager, login_user, logout_user
from flask import Blueprint, render_template, request, redirect
from flask_login.mixins import UserMixin

login_manager = LoginManager()
login_manager.login_view = 'bp_login.login'
bp_login = Blueprint('bp_login', __name__)

@login_manager.user_loader
def user_loader(user_id):
    user = UserMixin()
    user.id = user_id
    print(user)
    return user

@bp_login.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    user = UserMixin()
    user.id = 1
    login_user(user)
    return redirect('/')

@bp_login.route('/logout')
def logout():
    logout_user()
    return redirect('login')