from app import db
from flask_sqlalchemy import SQLAlchemy
import datetime

class Hobby(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    description = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(15), nullable=True)
    user_hobby = db.relationship('UserHobby', backref='hobby', lazy=True)
