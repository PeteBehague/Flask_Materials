from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange

class DogForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=2,max=15)])
    age = IntegerField("Age", validators=[ NumberRange(min=0, max=20)])
    breed = SelectField("Dog Breed", choices=[
        ("collie", "Collie"),
        ("retriever", "Retriever"),
        ("pug", "Pug")
    ])
    submit = SubmitField("Submit")