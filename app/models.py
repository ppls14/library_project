from app import db

from . import db

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

book_author = db.Table('book_author',
    db.Column('book_id', db.ForeignKey('book.id')),
    db.Column('author_id', db.ForeignKey('author.id'))
)

class Book(db.Model):
    __tablename__  = 'book'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), index = True)

    authors = db.relationship('Author', secondary = book_author, backref ='books', lazy = 'dynamic')
    is_available = db.Column(db.Boolean, default=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title
    
class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), unique = False)
    surname = db.Column(db.String(100), unique = False)

    def __str__(self):
        return f'{self.name} {self.surname}'

    def __repr__(self):
        return f'{self.name} {self.surname}'

class Borrow(db.Model):
    __tablename__ ='availability '
    id = db.Column(db.Integer, primary_key = True)
    book = db.Column(db.Integer, db.ForeignKey('book.id'))
    date_borrow = db.Column(db.String(10))
    date_return = db.Column(db.String(10))
    books = db.relationship('Book', backref = 'borrows')