from application import db

class Customers(db.Model):
    customerid = db.Column(db.Integer, primary_key=True)
    customername = db.Column(db.String(50))
    addressline1 = db.Column(db.String(100))
    addressline2 = db.Column(db.String(100))
    addressline3 = db.Column(db.String(100))
    postcode = db.Column(db.String(10))
    phone = db.Column(db.String(16))
    email = db.Column(db.String(100))
    securityquestion = db.Column(db.String(200))
    securityquestionanswer = db.Column(db.String(200))
