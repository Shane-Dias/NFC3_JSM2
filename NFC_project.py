from flask import Flask, render_template,request, session,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import check_password_hash
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

def sign_up():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        new_user = Users(username=username,email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/log-reg.html')
    
    return render_template("sign up")

def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Fetch the user by email
        user = Users.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            return redirect('/')
        else:
            return render_template('log-reg.html', error='Invalid email or password')


@app.route('/login',methods=['GET','POST'])
def check():
    data = request.form.get('username')
    if data==None:
        login()
    else:
        sign_up()
    return render_template("log-reg.html")




@app.route('/adoptpet/Dogs')
def adoptpet():
    return render_template('dog.html')


if __name__ == "__main__":
    app.run(debug=True)
