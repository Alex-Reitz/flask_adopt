from flask import Flask, request, render_template
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'ihaveasecret'

DebugToolbarExtension(app)
connect_db(app)
db.create_all()

@app.route("/")
def home_page():
    return render_template("home.html")