from application import app, db
from application.models import Customers

@app.route('/add')
def add():
    new_customer = Customers(customername="New Customer", addressline1="1 the High St", postcode="SW19 3FG", phone="123456", email="ted@ted.com", securityquestion="foo", securityquestionanswer="bar")
    db.session.add(new_customer)
    db.session.commit()
    return "Added new customer to database"

@app.route('/read')
def read():
    all_customers = Customers.query.all()
    customers_string = ""
    for customer in all_customers:
        customers_string += "<br>"+ customer.customername
    return customers_string

@app.route('/update/<name>')
def update(name):
    first_customer = Customers.query.first()
    first_customer.customername = name
    db.session.commit()
    return first_customer.customername