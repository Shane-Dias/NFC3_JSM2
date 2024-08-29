from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Import your models after initializing db
from Classes import Users, Dogs

@app.route('/')
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
