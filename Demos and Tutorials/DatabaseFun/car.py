from app import db

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number_plate = db.Column(db.String(7), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'), nullable=False)