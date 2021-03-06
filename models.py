from flask_login import UserMixin
from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash


# os.chdir('/users/maslah/documents/Python/bc-8-online-store')


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
    __tablename__ = 'store'
    id = db.Column('store_id', db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    title = db.Column(db.String(100))
    products = db.Column(db.Text)
    users = db.relationship(
                            Users,
                            backref=db.backref('stores', lazy='dynamic'))
    '''
    Defines the constructor for the stores class
    '''
    def __init__(self, title, products, user_id):
        self.title = title
        self.products = products

    def __repr__(self):
        return '<Store %r>' % self.title
