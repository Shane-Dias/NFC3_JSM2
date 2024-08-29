from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///default.db'
app.config["SQLALCHEMY_BINDS"] = {'db1': 'sqlite:///db1.db', 'db2': 'sqlite:///db2.db','db3': 'sqlite:///db3.db', 'db4': 'sqlite:///db4.db','db5': 'sqlite:///db5.db', 'db6': 'sqlite:///db6.db'}
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app) 
with app.app_context():
    db.create_all()
class Users(db.Model):
    __bind_key__="db1"
    __tablename__ = 'users'
    sno = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.now)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class Dogs(db.Model):
    __bind_key__="db2"
    __tablename__ = 'dogs'
    sno = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.now)
    name = db.Column(db.String(80), nullable=False)
    breed = db.Column(db.String(80), nullable=False)
    sex = db.Column(db.String(80), nullable=False)
    size = db.Column(db.Integer, nullable=False)
    desc = db.Column(db.String(200), nullable=False)

    def __init__(self, name, breed, sex, size, desc):
        self.name = name
        self.breed = breed
        self.sex = sex
        self.size = size
        self.desc = desc



class cats(db.Model):
    __bind_key__="db3"
    sno = db.Column(db.Integer, primary_key=True)
    date_created=db.Column(db.DateTime, default=datetime.now())
    name = db.Column(db.String(80),nullable=False)
    breed= db.Column(db.String(80),nullable=False)
    sex= db.Column(db.String(80),nullable=False)
    size = db.Column(db.Integer,nullable=False)
    desc = db.Column(db.String(200),nullable=False)
    def __init__(self, name, breed, sex, size, desc):
        self.name = name
        self.breed = breed
        self.sex = sex
        self.size = size
        self.desc = desc

class sea_creatures(db.Model):
    __bind_key__="db4"
    id = db.Column(db.Integer, primary_key=True)
    date_created=db.Column(db.DateTime, default=datetime.now())
    name = db.Column(db.String(80),nullable=False)
    typee=db.Column(db.String(80),nullable=False)
    breed= db.Column(db.String(80),nullable=False)
    sex= db.Column(db.String(80),nullable=False)
    size = db.Column(db.Integer,nullable=False)
    desc = db.Column(db.String(200),nullable=False)
    def __init__(self, name, breed, sex, size, desc):
        self.name = name
        self.breed = breed
        self.sex = sex
        self.size = size
        self.desc = desc

class oanimals(db.Model):
    __bind_key__="db5"
    id = db.Column(db.Integer, primary_key=True)
    date_created=db.Column(db.DateTime, default=datetime.now())
    name = db.Column(db.String(80),nullable=False)
    breed= db.Column(db.String(80),nullable=False)
    sex= db.Column(db.String(80),nullable=False)
    size = db.Column(db.Integer,nullable=False)
    desc = db.Column(db.String(200),nullable=False)


class history(db.Model):
    __bind_key__="db6"
    sno = db.Column(db.Integer, primary_key=True)
    date_created=db.Column(db.DateTime, default=datetime.now())
    username = db.Column(db.String(80),nullable=False)
    animalID= db.Column(db.String(80),nullable=False)
    animalName= db.Column(db.String(80),nullable=False)
    requestDate = db.Column(db.String(80),nullable=False)
    adoptionDate = db.Column(db.String(200),nullable=False)
    status = db.Column(db.String(200),nullable=False)

@app.route('/')
def hello_world():
    username = "lol21"
    password = "lmao"
    email = "mayankhmehta@gmail.com"
    #user = Users(username=username, password=password, email=email)
    #db.session.add(user)
    #db.session.commit()

    name = "Tillu"
    breed = "Golden Retriever"
    sex = "Male"
    size = 50
    desc = ("Tillu is a wonderful and lovable creature. As hard as it can be to donate the pet, "
            "the circumstances equally demand. I'm preparing for an exam and I would be away from "
            "home most of the time. Tillu gets anxious meanwhile and that's why I want to donate my pet.")
    #dog = Dogs(name=name, breed=breed, sex=sex, size=size, desc=desc)
    #db.session.add(dog)
    #db.session.commit()

    return render_template("templates")

@app.route('/login')
def login():
    return "login"


@app.route('/sign_up')
def sign_up():
    return "sign up"


@app.route('/adoptpet')
def adoptpet():
    return "adopt pet"


if __name__ == "__main__":
    app.run(debug=True)
