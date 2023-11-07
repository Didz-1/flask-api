from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://ykxoicvl:WAdhNy8kaOA4ESJbH_nhH78IG6jQJFH-@trumpet.db.elephantsql.com/ykxoicvl"
db = SQLAlchemy(app)

from application import routes

