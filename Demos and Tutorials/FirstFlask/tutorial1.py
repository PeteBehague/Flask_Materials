from flask import Flask, request, redirect, url_for, render_template
#Importing Libraries
from flask import Flask,jsonify
from flask_restful import  Api, Resource
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
application=app
api = Api(app)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite3'


class User(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(100), nullable=True)
    email = db.Column('email', db.String(100), nullable=True)
    phone = db.Column('phone', db.String(100), nullable=True)

    def __init__(self, id, name, email, phone="11111111"):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone


    db.create_all()


class save(Resource):
    def get(self):
        name = request.form.get("name")
        if name:
            pass
        else:
            name = request.args.get("name")
        email = request.form.get("email")
        if email:
            pass
        else:
            email = request.args.get("email")
        phone = request.form.get("phone")
        if phone:
            pass
        else:
            phone = request.args.get("phone")
        if User.query.filter_by(email=email).first() or User.query.filter_by(phone=phone).first():
            return jsonify({"success": False, "message": "Email already saved"})
        user = User(name=name, email=email)
        db.session.add(user)
        db.session.commit()

        return jsonify({"success": True, "message": "data saved"})

@app.route("/")
def home():
    return render_template("index.html", content="Testing")


# @app.route("/<name>")
# def user(name):
#     return  f"Hello {name}!"
#
# @app.route("/admin/")
# def admin():
#     return redirect(url_for("user", name="Ted!"))

if __name__ == '__main__':
    app.run(debug=True)
