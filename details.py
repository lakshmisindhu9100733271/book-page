from datetime import datetime as dt
from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()
class Detail(db.Model):
    __tablename__ = "detail"

    email = db.Column(db.String(120),primary_key=True)
    isbn = db.Column(db.String(80),primary_key=True)
    rating = db.Column(db.String(80),nullable=False)
    review = db.Column(db.String(80),nullable=False)
    timestrap=db.Column(db.DateTime,nullable=False)


    def __init__(self,email,isbn,rating,review):
        self.email = email
        self.isbn=isbn
        self.rating=rating
        self.review=review
        self.timestrap=dt.now()