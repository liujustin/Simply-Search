from flask_wtf import FlaskForm
from wtforms import (PasswordField,
                     StringField,
                     SubmitField,
                     ValidationError)
from wtforms.validators import (DataRequired,
                                Email,
                                EqualTo)
from ..models import User


class RegistrationForm(FlaskForm):
    """
    Form for users to create new account
    """

    email = StringField('Email', validators=[DataRequired(),
                                             Email()])
    username = StringField('Username', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     EqualTo('password_confirmation')])
    password_confirmation = PasswordField('Confirm Password')
    submit = SubmitField('Register')

    def validate_email(self, field):
        """
        Validate if email exists in database
        """

        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use.')

    def validate_username(self, field):
        """
        Validate if username exists in database
        """

        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username is already in use.')


class LoginForm(FlaskForm):
    """
    Form for users to login
    """
    
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
