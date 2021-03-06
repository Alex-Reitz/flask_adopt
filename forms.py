from flask_wtf import FlaskForm
from wtforms import StringField, FloatField

class AddPetForm(FlaskForm):
    name=StringField("Pet Name")
    species=StringField("Species name")
    Photo_url=StringField("Photo URL")
    age=FloatField("Age")
    notes=StringField("Notes about this pet")