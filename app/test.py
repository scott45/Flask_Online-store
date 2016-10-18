from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

class Stores(db.Model):
    '''
    Defines the store model which will be mapped
    to the store table in the db
    '''
    __tablename__ = 'stores'
    id = db.Column('store_id', db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    classification = db.Column(db.String(15))
    products = db.Column(db.Text)
    user = db.relationship(User, backref=db.backref('stores', lazy='dynamic'))
    '''
    Defines the constructor for the stores class
    '''
    def __init__(self, classification, Products, user_id):
        self.classification = classification
        self.products = Products

    def __repr__(self):
        return '<Store %r>' % self.classification

class Products(db.Model):
    '''
    Defines the product model which will be mapped
    to the product table in the db
    '''
    __tablename__ = 'products'
    id = db.Column('product_id', db.Integer, primary_key=True)
    classification = db.Column(db.String(40))
    Products = db.Column(db.Text)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.store_id'))
    # stores = db.relationship(
    #                         Stores,
    #                         backref=db.backref('Products', lazy='dynamic'))

    '''
    Defines the constructor for the products class
    '''
    def __init__(self, classification, store_id, Products):
        self.classification = classification
        self.store_id = store_id
        self.products = Products

    def __repr__(self):
        return '<Product %r>' % self.classification



if __name__ == '__main__':
    manager.run()