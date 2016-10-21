from flask_wtf import Form
from wtforms import StringField
from wtforms import SubmitField, validators


class ProductForm(Form):
    '''This class creates an ProductForm
    object.
    '''
# a store has a name and a description
    name = StringField('Product',
                       [validators.Required(message=' '),)
                       ]
                       )
    submit = SubmitField('Add Product')

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        