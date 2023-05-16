from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:Pa$$w0rd@35.246.27.133:3306/deansbeans"

db = SQLAlchemy(app)

from application import routes