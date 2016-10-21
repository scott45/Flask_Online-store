from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'index.html'

@app.route('/register')
def register():
    return 'register.html'

@app.route('/available_store')
def stores():
    return 'available_store.html'


@app.route('/available_product')
def products():
    return 'available_product.html'


@app.route('/add_product')
def adds():
    return 'add_product.html'

@app.route('/add_store')
def add():
    return 'add_store.html'

'''
@app.route('/')
def 

'''

if __name__ == '__main__':
    app.run()
