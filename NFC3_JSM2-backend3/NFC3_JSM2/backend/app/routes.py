from flask import Blueprint, render_template

routes = Blueprint('routes', __name__)

@routes.route('/login')
def login():
    return render_template('login.html')

@routes.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')

@routes.route('/adoptpet')
def adoptpet():
    return render_template('adoptpet.html')

@routes.route('/')
def hello_world():
    return "hello_world"