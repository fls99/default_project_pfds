from . import db 
from flask_login  import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # associate different information for users
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #must pass a valid user id. One user can have many notes. One to many relationship

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) # unique identifier
    email = db.Column(db.String(150), unique=True) 
    password = db.Column(db.String(150))
    first_name= db.Column(db.String(150))
    # want to find all notes from a user 
    notes = db.relationship('Note')