from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms import BooleanField, SubmitField, ValidationError, validators
from ..models import Users


class LoginForm(Form):
    '''This class creates a login form
    '''
    # for a login, the username and password are required.
    # remember is the result of the checkbox written
    # 'keep me logged in'
    username = StringField('Username',
                           [validators.Required(
                           )]
                           )
    password = PasswordField('Password', [validators.Required()])
    submit = SubmitField('Submit')


class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])
    submit = SubmitField('Submit')
    remember = None

    def validate_username(self, field):
        '''This method checks if a username already exists in
        the database
        '''
        # check fot the first occurrence of that username and raise an error
        if Users.query.filter_by(username=field.data).first():
            raise ValidationError('Username already exists.')