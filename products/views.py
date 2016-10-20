from flask import render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user, session
from . import product
from .. import db
from ..models import Stores, Products, Users
from .forms import ProductForm


@product.route('/home')
@login_required
def index():
    '''This view function displays
    stores records in the database.
    '''
    store = Stores.query.filter_by(user_id=current_user.id).first()
    products_instance = store.products.all()

    available_products = 0
    for i in products_instance:
        available_products += 1
    # import ipdb; ipdb.set_trace()
    return render_template('products/index.html', products_=products_instance,
                           available_products=available_products)


@product.route('/product/<username>/<storeId>')
def store_url(store_username, storeId):
    user = Users.query.filter_by(id=current_user.id)
    store_username = user.username
    store = Stores.query.filter_by(user_id=current_user).first()
    storeId = store.id
    with product.test_request_context():
        return render_template('store/index.html', store_username=store_username, storeId=storeId)


@product.route('/add_product', methods=['GET', 'POST'])
def product():
    '''This view function creates a
    new product record
    '''
    form = ProductForm()
    if form.validate_on_submit():
        store = Stores.query.filter_by(user_id=current_user.id).first()
        product_instance = Products(name=form.name.data,
                                    description=form.description.data,
                                    store_id=.id)
        # import ipdb; ipdb.set_trace()
        # store.products.append(product_instance)
        db.session.add(product_instance)
        db.session.commit()
