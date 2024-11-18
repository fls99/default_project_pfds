from . import db 
from flask_login  import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) # unique identifier
    email = db.Column(db.String(150), unique=True) 
    password = db.Column(db.String(150))
    first_name= db.Column(db.String(150))

class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    admin_level = db.Column(db.Integer, default=1)  # 1 is the lowest level of admin

class SeatingChart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    created_date = db.Column(db.DateTime(timezone=True), default=func.now())
    seats = db.relationship('Seat', backref='seating_chart', cascade='all, delete-orphan') # holds the relation for a seating chart for a particular file

class Seat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    row_number = db.Column(db.Integer, nullable=False)
    column_letter = db.Column(db.String(1), nullable=False)
    is_occupied = db.Column(db.Boolean, default=False)
    seat_type = db.Column(db.String(20))  # e.g. 'window', 'aisle', 'middle'
    date_modified = db.Column(db.DateTime(timezone=True), default=func.now())
    seating_chart_id = db.Column(db.Integer, db.ForeignKey('seating_chart.id'), nullable=False)
    