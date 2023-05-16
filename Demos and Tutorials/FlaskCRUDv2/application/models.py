from application import db, login_manager
from flask_login import UserMixin

class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return ''.join(['UserID: ', str(self.id), '\r\n',
        'Email: ', self.email], '\r\n',
        'Name: ', self.first_name, ' ', self.last_name
        )

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))