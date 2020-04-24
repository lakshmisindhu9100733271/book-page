from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as dt
# Set up database

db = SQLAlchemy()

class Users(db.Model) :
    __tablename__ = "Users"
    username = db.Column(db.String, primary_key = True)
    password = db.Column(db.String, nullable = False)
    email = db.Column(db.String, nullable = True)
    gender = db.Column(db.String, nullable = False)
    time = db.Column(db.DateTime, nullable = False)

    def __init__(self, username, password, email, gender):
        self.username = username
        self.password = password
        self.email = email
        self.gender = gender
        self.time = dt.now()
