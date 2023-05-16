from flask import Flask, redirect, render_template, request
from application.forms import RegisterForm
from application import db
from application.models import Register
from application import app


@app.route('/', methods=["GET","POST"])
def home():
    form = RegisterForm()
    if form.validate_on_submit():
        if not form.name.data is None and form.name.data != '':
            person = Register(name=form.name.data)
            db.session.add(person)
            db.session.commit()
    registrees = Register.query.all()
    return render_template("home.html", registrees=registrees, form=form)