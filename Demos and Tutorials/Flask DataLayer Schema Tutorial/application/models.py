from application import db
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
import os

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
    orders = db.relationship('Orders',backref='customer')

class Orders(db.Model):
        orderid = db.Column(db.Integer, primary_key=True)
        customerid = db.Column(db.Integer, db.ForeignKey('customers.customerid'), nullable=False)
        orderdate = db.Column(db.DateTime)
        ordertotal = db.Column(db.Float)
        orderstatus = db.Column(db.Integer)



