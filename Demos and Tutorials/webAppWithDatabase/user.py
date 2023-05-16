from app import db
from flask_sqlalchemy import SQLAlchemy
import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(15), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    dob = db.Column(db.DateTime, nullable=False)
    favourite_number = db.Column(db.Float, nullable=True)
    favourite_food = db.Column(db.String(3), default='MEX', nullable=False)
    user_hobby = db.relationship('UserHobby', backref='user', lazy=True)
