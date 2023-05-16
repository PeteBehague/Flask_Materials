from app import db
from user import User
from hobby import Hobby
from user_hobby import UserHobby
import datetime

db.drop_all()
db.create_all()

testuser1 = User(first_name='Elizabeth', last_name='Windsor', dob=datetime.datetime(1917, 4, 23))
db.session.add(testuser1)
testuser2 = User(first_name='Charles', last_name='Windsor', dob=datetime.datetime(1941, 5, 17))
db.session.add(testuser2)
testuser3 = User(first_name='Philip', last_name='Windsory', dob=datetime.datetime(1912, 7, 27))
db.session.add(testuser3)
testuser4 = User(first_name='William', last_name='Windsor', dob=datetime.datetime(1987, 11, 17))
db.session.add(testuser4)
testuser5 = User(first_name='Harry', last_name='Windsor', dob=datetime.datetime(1990, 9, 5))
db.session.add(testuser5)


testhobby1 = Hobby(name='Woodwork', description='Lots of sawing and planing')
db.session.add(testhobby1)
testhobby2 = Hobby(name='Singing', description='The hills are alive!')
db.session.add(testhobby2)


testuser_hobby1 = UserHobby(user_id=testuser1.id, hobby_id=testhobby1.id)
db.session.add(testuser_hobby1)
testuser_hobby2 = UserHobby(user_id=testuser2.id, hobby_id=testhobby1.id)
db.session.add(testuser_hobby2)
testuser_hobby2 = UserHobby(user_id=testuser2.id, hobby_id=testhobby2.id)
db.session.add(testuser_hobby2)

db.session.commit()

user = User.query.order_by(User.first_name.desc()).first()
# for user in users:


db.session.delete(user)
db.session.commit()

users = User.query.all()
for user in users:
    print(user.id, user.first_name, user.last_name)
