from app import db
from user import User
from car import Car
from owner import Owner

db.drop_all()
db.create_all()

testuser1 = User(first_name='Grooty',last_name='Toot') # Extra: this section populates the table with an example entry
db.session.add(testuser1)
testuser2 = User(first_name='Tooty',last_name='Toot') # Extra: this section populates the table with an example entry
db.session.add(testuser2)

testowner1 = Owner(first_name='Susie',last_name='Sparkle')
db.session.add(testowner1)
testowner2 = Owner(first_name='Sadia',last_name='Saleem')
db.session.add(testowner2)

testcar1 = Car(number_plate='ABC 123', owner_id=1)
db.session.add(testcar1)
testcar2 = Car(number_plate='XYZ 987', owner_id=2)
db.session.add(testcar2)
testcar3 = Car(number_plate='DEF 567', owner_id=1)
db.session.add(testcar3)

db.session.commit()

print(testowner1.cars)
print(testcar1.ownerbr.first_name, testcar1.ownerbr.last_name, testcar2.ownerbr.first_name, testcar2.ownerbr.last_name)

cars = Car.query.order_by(Car.number_plate).all()
for car in cars:
    print(car.number_plate)

car = Car.query.filter_by(number_plate="DEF 567").first()
car.number_plate = "NNN 111"
db.session.commit()
cars = Car.query.order_by(Car.number_plate).all()
for car in cars:
    print(car.number_plate)

db.session.delete(car)
db.session.commit()

cars = Car.query.order_by(Car.number_plate).all()
print("car removed:")
for car in cars:
    print(car.number_plate)


#print(car.owner_id)
#owner = Owner.query.get(car.owner_id)
#print(owner.first_name, owner.last_name)
