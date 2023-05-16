from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '2adec9303f70b68b97b6d1e814f07a46'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///games.db"

db = SQLAlchemy(app)

from application import routes