from flask import Flask
from app import app, db
from sqlalchemy import create_engine
from flask_login import UserMixin
from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash



engine = create_engine('sqlite:///db/scott.db')

class Users(db.Model, UserMixin):
    '''
    Defines the user model which will be mapped
    to the user table in the db
    '''
    __tablename__ = 'users'
    id = db.Column('user_id', db.Integer, primary_key=True)
    fname = db.Column(db.String(20))
    lname = db.Column(db.String(20))
    username = db.Column(db.String(50), unique=True, index=True)
    password = db.Column(db.String(128))
    phone = db.Column(db.String(10))
    # stores = db.relationship('Stores', backref='users')

    '''
    Defines the constructor for the users class
    '''
    def __init__(self, fname, lname, username, password, phone):
        self.fname = fname
        self.lname = lname
        self.username = username
        self.phone = phone
        self.set_password(password)

    def set_password(self, password_hash):
        '''Sets password to a hashed password
        '''
        self.password = generate_password_hash(password_hash)

    def verify_password(self, password_hash):
        '''Checks if password matches
        '''
        return check_password_hash(self.password, password_hash)

        '''
        The __repr__() method is made automatically when the class is made,
        it decides how the class is represented when it is printed
        '''
    def __repr__(self):
        return '<Users %r>' % self.id


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Stores(db.Model):
    '''
    Defines the store model which will be mapped
    to the store table in the db
    '''
    __tablename__ = 'stores'
    id = db.Column('store_id', db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    classification = db.Column(db.String(15))
    products = db.Column(db.Text)
    users = db.relationship(Users, backref=db.backref('stores', lazy='dynamic'))
    '''
    Defines the constructor for the stores class
    '''
    def __init__(self, Classification, Products, users_id):
        self.Classification = Classification
        self.products = Products

    def __repr__(self):
        return '<Store %r>' % self.Classification


class Products(db.Model):
    '''
    Defines the product model which will be mapped
    to the product table in the db
    '''
    __tablename__ = 'products'
    id = db.Column('product_id', db.Integer, primary_key=True)
    Classification = db.Column(db.String(40))
    Products = db.Column(db.Text)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.store_id'))
    # stores = db.relationship(
    #                         Stores,
    #                         backref=db.backref('Products', lazy='dynamic'))

    '''
    Defines the constructor for the products class
    '''
    def __init__(self, Classification, store_id, Products):
        self.Classification = Classification
        self.store_id = store_id
        self.Products = Products

    def __repr__(self):
        return '<Product %r>' % self.Classification


