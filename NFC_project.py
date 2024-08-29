from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///default.db'
app.config["SQLALCHEMY_BINDS"] = {
    'db1': 'sqlite:///db1.db', 
    'db2': 'sqlite:///db2.db',
    'db3': 'sqlite:///db3.db', 
    'db4': 'sqlite:///db4.db',
    'db5': 'sqlite:///db5.db', 
    'db6': 'sqlite:///db6.db'
}
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Users(db.Model):
    __bind_key__ = "db1"
    sno = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.now)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class oanimals(db.Model):
    __bind_key__ = "db2"
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    breed = db.Column(db.String(80), nullable=False)
    sex = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer,nullable=False)
    size = db.Column(db.String(80), nullable=False)
    desc = db.Column(db.String(200), nullable=False)
    def __init__(self, name, breed, sex,age,size,desc):
        self.name = name
        self.breed = breed
        self.sex = sex
        self.age = age
        self.size = size
        self.desc = desc

class cats(db.Model):
    __bind_key__ = "db3"
    sno = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.now)
    name = db.Column(db.String(80), nullable=False)
    breed = db.Column(db.String(80), nullable=False)
    sex = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer,nullable=False)
    size = db.Column(db.String(80), nullable=False)
    desc = db.Column(db.String(200), nullable=False)
    def __init__(self, name, breed, sex,age,size,desc):
        self.name = name
        self.breed = breed
        self.sex = sex
        self.age = age
        self.size = size
        self.desc = desc

class sea_Creatures(db.Model):
    __bind_key__ = "db4"
    sno = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.now)
    name = db.Column(db.String(80), nullable=False)
    breed = db.Column(db.String(80), nullable=False)
    sex = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer,nullable=False)
    size = db.Column(db.String(80), nullable=False)
    desc = db.Column(db.String(200), nullable=False)
    def __init__(self, name, breed, sex,age,size,desc):
        self.name = name
        self.breed = breed
        self.sex = sex
        self.age = age
        self.size = size
        self.desc = desc

class dogs(db.Model):
    __bind_key__ = "db5"
    sno = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.now)
    name = db.Column(db.String(80), nullable=False)
    breed = db.Column(db.String(80), nullable=False)
    sex = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer,nullable=False)
    size = db.Column(db.String(80), nullable=False)
    desc = db.Column(db.String(200), nullable=False)
    def __init__(self, name, breed, sex,age,size,desc):
        self.name = name
        self.breed = breed
        self.sex = sex
        self.age = age
        self.size = size
        self.desc = desc

class history(db.Model):
    __bind_key__ = "db6"
    sno = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.now)
    name = db.Column(db.String(80), nullable=False)
    breed = db.Column(db.String(80), nullable=False)
    sex = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer,nullable=False)
    size = db.Column(db.String(80), nullable=False)
    desc = db.Column(db.String(200), nullable=False)
    def __init__(self, name, breed, sex,age,size,desc):
        self.name = name
        self.breed = breed
        self.sex = sex
        self.age = age
        self.size = size
        self.desc = desc

with app.app_context():
    db.create_all()

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("log-reg.html")


@app.route('/sign_up')
def sign_up():
    return "sign up"


@app.route('/adoptpet')
def adoptpet():
    return "adopt pet"


if __name__ == "__main__":
    app.run(debug=True)