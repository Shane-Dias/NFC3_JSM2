from flask import Flask, redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


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

# Initialize tables within app context
with app.app_context():
    db.create_all()

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
        email = request.form['email']
        password = request.form['password']

        new_user = Users(email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/log-reg.html')
    
    return render_template("sign up")



@app.route('/adoptpet')
def adoptpet():
    if session['email']:
        return render_template("adopt pet")
    
    return redirect('/log-reg.html')


if __name__ == "__main__":
    app.run(debug=True)
