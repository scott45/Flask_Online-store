from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms import SubmitField, validators


class StoreForm(Form):
    '''This class creates an StoreForm
    object.
    '''
# a store has a name and a description
# a store belongs to a user
    title = StringField('Store',
                       [validators.Required)
                        validators.Length(
                           max=70,
                           message='Store title is too long.'
                       )
                       ]
                       )
    Products = TextAreaField('Products',
                                [validators.required])
    submit = SubmitField('Save')

    def __init__(self, *args, **kwargs):
        super(StoreForm, self).__init__(*args, **kwargs)