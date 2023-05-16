from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField

class DogForm(FlaskForm):
    name = StringField("Name")
    age = IntegerField("Age")
    breed = SelectField("Dog Breed", choices=[
        ("collie", "Collie"),
        ("retriever", "Retriever"),
        ("pug", "Pug")
    ])
    submit = SubmitField("Submit")