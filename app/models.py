from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from flask_login import UserMixin


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class User(db.Model, UserMixin):
    '''
    Defines the user model which will be mapped
    to the user table in the db
    ''' 
    __tablename__ = 'user'
    id = db.Column('user_id', db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    email = db.Column(db.String(20))
    # stores = db.relationship('Stores', backref='users')

    '''
    Defines the constructor for the user class
    '''
    def __init__(self, name, email):
        self.name = fname
        self.email= lname

    def __repr__(self):
        return '<Store %r>' % self.name
class Stores(db.Model):
    '''
    Defines the store model which will be mapped
    to the store table in the db
    '''
    __tablename__ = 'store'
    id = db.Column('store_id', db.Integer, primary_key=True)
    Title = db.Column(db.String(20))
    Owner =db.ForeignKey('user.user_id'))
    is_favorite = db.BooleanField(default=False)
    '''
    Defines the constructor for the store class
    '''
    def __init__(self, Title, Owner, is_favorite):
        self.title = Title
        self.Owner = Owner
        self.is_favorite = is_favorite

    def __repr__(self):
        return '<Store %r>' % self.title

 __tablename__ = 'product'
    id = db.Column('store_id', db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    Category =db.ForeignKey('store.store_id'))
    is_favorite = db.BooleanField(default=False)
    '''
    Defines the constructor for the product class
    '''
    def __init__(self, Title, Owner, is_favorite):
        self.name = name
        self.Category = Category
        self.is_favorite = is_favorite

    def __repr__(self):
        return '<Store %r>' % self.name



if __name__ == '__main__':
    manager.run()