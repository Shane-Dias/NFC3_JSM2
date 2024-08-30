from flask import Flask, render_template,request, url_for,redirect
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

class Cat(db.Model):
    __bind_key__ = "db3"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    breed = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_filename = db.Column(db.String(255))  # Store the filename of the uploaded image

    def __init__(self, name, age, breed, description, image_filename=None):
        self.name = name
        self.age = age
        self.breed = breed
        self.description = description
        self.image_filename = image_filename

class Dog(db.Model):
    __bind_key__ = "db5"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    breed = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_filename = db.Column(db.String(255))  # Store the filename of the uploaded image

    def __init__(self, name, age, breed, description, image_filename=None):
        self.name = name
        self.age = age
        self.breed = breed
        self.description = description
        self.image_filename = image_filename



with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template("index.html")



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
def sign_up():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        new_user = Users(username=username,email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("log-reg.html")

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/PetSitter')
def petsitter():
    return render_template("petsitter.html")

@app.route('/adoptpet/Dogs')
def adoptdogs():
    return render_template('dog.html')

@app.route('/adoptpet/Cats')
def adoptcats():
    return render_template('cat.html')

@app.route('/dog/<int:dog_id>')
def dog_details(dog_id):
    dog = Dog.query.get_or_404(dog_id)
    return render_template('dog_details.html', dog=dog)

@app.route('/cat/<int:cat_id>')
def cat_details(cat_id):
    cat = Cat.query.get_or_404(cat_id)
    return render_template('cat_details.html', cat=cat)

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

@app.route('/adopt/<int:animal_id>', methods=['POST'])
def adopt_animal():
    # Add your adoption logic here
    # For example, you might want to mark the animal as adopted or add an entry in a history table
    # This is a placeholder implementation
    return redirect('/thank_you')

@app.route('/shelterInformation')
def shelterinfo():
    return render_template('shelter.html')

if __name__ == "__main__":
    app.run(debug=True)
