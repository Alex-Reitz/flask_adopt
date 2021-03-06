from flask import Flask, request, render_template, flash, redirect
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm

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

@app.route("/add", methods=["GET", "POST"])
def add_form():

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        flash(f"Added {name} of {species}")
        return redirect("/add")
    else:
        return render_template("add_form.html", form=form)