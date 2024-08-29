from flask import Flask, redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from werkzeug.utils import secure_filename


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

# Define models
class Users(db.Model):
    __bind_key__ = "db1"
    sno = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.now)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)

    def __init__(self, username, password, email,):
        self.username = username
        self.password = password
        self.email = email

# Other models (Dogs, cats, sea_creatures, oanimals, history) follow the same pattern...
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


# Initialize tables within app context
with app.app_context():
    db.create_all()

# Directory where uploaded files will be stored
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit upload size to 16 MB
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/add_cat', methods=['GET', 'POST'])
def add_cat():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        breed = request.form['breed']
        description = request.form['description']
        image = request.files.get('image')

        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image.save(image_path)
        else:
            filename = None

        new_cat = Cat(name=name, age=age, breed=breed, description=description, image_filename=filename)
        db.session.add(new_cat)
        db.session.commit()
        return redirect('/cats')
    
    # Return the form for adding a cat if the request method is GET
    return render_template('add_cat.html')


@app.route('/cats')
def list_cats():
    cats = Cat.query.all()
    return render_template('cats.html', cats=cats)

@app.route('/cat/<int:cat_id>')
def cat_details(cat_id):
    cat = Cat.query.get_or_404(cat_id)
    return render_template('cat_details.html', cat=cat)

@app.route('/delete_cat/<int:cat_id>', methods=['POST'])
def delete_cat(cat_id):
    cat = Cat.query.get_or_404(cat_id)
    db.session.delete(cat)
    db.session.commit()
    return redirect('/cats')

@app.route('/add_dog', methods=['GET', 'POST'])
def add_dog():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        breed = request.form['breed']
        description = request.form['description']
        image = request.files.get('image')

        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image.save(image_path)
        else:
            filename = None

        new_dog = Dog(name=name, age=age, breed=breed, description=description, image_filename=filename)
        db.session.add(new_dog)
        db.session.commit()
        return redirect('/dogs')
    
    return render_template('add_dog.html')

@app.route('/dogs')
def list_dogs():
    dogs = Dog.query.all()
    return render_template('dogs.html', dogs=dogs)

@app.route('/dog/<int:dog_id>')
def dog_details(dog_id):
    dog = Dog.query.get_or_404(dog_id)
    return render_template('dog_details.html', dog=dog)

@app.route('/delete_dog/<int:dog_id>', methods=['POST'])
def delete_dog(dog_id):
    dog = Dog.query.get_or_404(dog_id)
    db.session.delete(dog)
    db.session.commit()
    return redirect('/dogs')

@app.route('/')
def hello_world():
     # Return the template
    return render_template("index.html")

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = Users.query.filter_by(email = email).first()

        if user and user.check_password(password):
            session['email'] = user.email
            session['password'] = user.password
            return redirect('/index')
        else:
            return render_template('/log-reg.html',error='Invalid User')

    return render_template("log-reg.html")


@app.route('/sign_up',methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        new_user = Users(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/log-reg.html')
    
    return render_template("sign up")

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

@app.route('/adopt/<int:animal_id>', methods=['POST'])
def adopt_animal(animal_id):
    # Add your adoption logic here
    # For example, you might want to mark the animal as adopted or add an entry in a history table
    # This is a placeholder implementation
    return redirect('/thank_you')

@app.route('/adoptpet')
def adoptpet():
    if session['email']:
        user = Users.query.filter_by(email=session['email']).first()
        return render_template("adopt pet")
    
    return redirect('/log-reg.html')

@app.route('/logout')
def logout():
    session.pop('email',None)
    return redirect('/log-reg.html')


if __name__ == "__main__":
    app.run(debug=True)