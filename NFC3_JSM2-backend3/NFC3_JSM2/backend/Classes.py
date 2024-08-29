from app import db
from datetime import datetime

class Users(db.Model):
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
    id = db.Column(db.Integer, primary_key=True)
    date_created=db.Column(db.DateTime, default=datetime.now())
    name = db.Column(db.String(80),nullable=False)
    breed= db.Column(db.String(80),nullable=False)
    sex= db.Column(db.String(80),nullable=False)
    size = db.Column(db.Integer,nullable=False)
    desc = db.Column(db.String(200),nullable=False)


class history(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    date_created=db.Column(db.DateTime, default=datetime.now())
    username = db.Column(db.String(80),nullable=False)
    animalID= db.Column(db.String(80),nullable=False)
    animalName= db.Column(db.String(80),nullable=False)
    requestDate = db.Column(db.String(80),nullable=False)
    adoptionDate = db.Column(db.String(200),nullable=False)
    status = db.Column(db.String(200),nullable=False)

def hello_world():
    username = "lol21"
    password = "lmao"
    email = "mayankhmehta@gmail.com"
    user = Users(username=username, password=password, email=email)
    db.session.add(user)
    db.session.commit()

    name = "Tillu"
    breed = "Golden Retriever"
    sex = "Male"
    size = 50
    desc = ("Tillu is a wonderful and lovable creature. As hard as it can be to donate the pet, "
            "the circumstances equally demand. I'm preparing for an exam and I would be away from "
            "home most of the time. Tillu gets anxious meanwhile and that's why I want to donate my pet.")
    dog = Dogs(name=name, breed=breed, sex=sex, size=size, desc=desc)
    db.session.add(dog)
    db.session.commit()

    return "Hello World"