from app import db
from flask_sqlalchemy import SQLAlchemy

class UserHobby(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hobby_id = db.Column('hobby_id', db.Integer, db.ForeignKey('hobby.id'))
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
