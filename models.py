import os
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

from dotenv import load_dotenv

load_dotenv()

dbUser = os.getenv("DB_USER")
dbPwd = os.getenv("DB_PWD")
dbName = os.getenv("DB_NAME")
dbHost = os.getenv("DB_HOST")
'''
database_path = os.environ['DATABASE_URL']
if database_path.startswith("postgres://"):
  database_path = database_path.replace("postgres://", "postgresql://", 1)
'''

database_path = "postgresql://{}:{}@{}/{}".format(
    dbUser, dbPwd, dbHost, dbName)

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
Person
Have title and release year
'''


class Person(db.Model):
    __tablename__ = 'People'

    id = Column(db.Integer, primary_key=True)
    name = Column(String)
    catchphrase = Column(String)

    def __init__(self, name, catchphrase=""):
        self.name = name
        self.catchphrase = catchphrase

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'catchphrase': self.catchphrase}


class Movie(db.Model):
    __tablename__ = 'movie'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(DateTime, nullable=False)
    genre_id = Column(Integer, ForeignKey('genres.id'), nullable=False)

    def __init__(self, title, release_date, genre_id):
        self.title = title
        self.release_date = release_date
        self.genre_id = genre_id

    def insert(self):
        db.session.add(self)
        db.session.flush()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.flush()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
            'genre_id': self.genre_id
        }
    # -----------------------------------------------


class Genres(db.Model):
    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True)
    genre = Column(String, nullable=False)

    def __init__(self, genre):
        self.genre = genre

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'genre': self.genre
        }
    # -----------------------------------------------


class Artist(db.Model):
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    # -------------------------------------------------
    artistfilm = db.relationship('MatchTable', backref='artistfilm', lazy=True)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }


# MatchTable is association table
class MatchTable(db.Model):
    __tablename__ = 'matchtable'

    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey(
        'artist.id'), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)

    def __init__(self, artist_id, movie_id):
        self.artist_id = artist_id
        self.movie_id = movie_id

    def insert(self):
        db.session.add(self)
        db.session.flush()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.flush()
