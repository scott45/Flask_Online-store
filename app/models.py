from flask import Flask
from app import app, db
from sqlalchemy import create_engine


engine = create_engine('sqlite:///db/scott.db')

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(60), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


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
    def __init__(self, Classification, Products, user_id):
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


