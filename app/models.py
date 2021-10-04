from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin
from datetime import datetime 
import uuid 
from secrets import token_hex

from werkzeug.security import generate_password_hash

login = LoginManager()

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


db = SQLAlchemy()

class Movie(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    movie = db.Column(db.String(200))
    protagonist = db.Column(db.String(150), nullable=False, unique=True)
    antagonist = db.Column(db.String(150), nullable=False, unique=True)
    other_characters = db.Column(db.String(150), nullable=False)
    movie_released = db.Column(db.INTEGER)
    actor = db.Column(db.INTEGER)


    def to_dict(self):
        return {
            'id': self.id,
            'movie': self.movie,
            'protagonist': self.protagonist,
            'antagonist': self.antagonist,
            'other_characters': self.other_characters,
            'movie_released': self.movie_released,
            'actor':self.actor
        }

    def from_dict(self, new):
        if new.get('id'):
            self.id = new.get('id')
        if new.get('protagonist'):
            self.protagonist = new.get('protagonist')
        if new.get('antagonist'):
            self.antagonist = new.get('antagonist')
        if new.get('movie') or new.get('movie') == '':
            self.movie = new.get('movie')
        if new.get('movie_released') or new.get('movie_released') == '':
            self.movie_released = new.get('movie_released')
        if new.get('actor') or new.get('actor') == '':
            self.actor = new.get('actor')
        return self


class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False, default='')  
    first_name = db.Column(db.String(200), nullable=True, default='')
    last_name = db.Column(db.String(200), nullable=True, default='')
    apitoken = db.Column(db.String(32), nullable=True, default=None)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, username, email, password, first_name='', last_name=''):
        self.username = username
        self.email = email.lower()
        self.password = generate_password_hash(password)
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.id = str(uuid.uuid4())
        self.apitoken=token_hex(16)


    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'date_created': self.date_created

        }