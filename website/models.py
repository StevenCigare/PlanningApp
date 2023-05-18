from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10000))
    date = db.Column(db.Date, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    completed = db.Column(db.Boolean, default=False, nullable=False)
    #hour = db.Column(db.String(1000))
    

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
    #current_date_notes = db.relationship('Note', post_update=False)
    chosen_date = db.Column(db.Date, nullable = False, default=func.current_date())

    def __repr__(self):
        return '<Email %r>' % self.email