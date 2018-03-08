from flask import (
    flash,
    redirect,
    render_template,
    url_for
)
from flask_login import (
    login_required,
    login_user,
    logout_user
)
from forms import LoginForm, RegistrationForm

from . import auth
from .. import db
from ..models import User


@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handles requests to and from register route form and adds user to database 
    """

    registration_form = RegistrationForm()
    if registration_form.validate_on_submit():
        user = User(email=registration_form.email.data,
                    username=registration_form.username.data,
                    first_name=registration_form.first_name.data,
                    last_name=registration_form.last_name.data,
                    password=registration_form.password.data)

        # adding a user to the database
        db.session.add(user)
        db.session.commit()
        flash('You have been successfully registered!')

        # redirect to the login page
        return redirect(url_for('home.search'))

    return render_template('auth/register.html', form=registration_form, title='Register')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handles requests to and from login route form and attempts to log a user in
    """

    login_form = LoginForm()
    if login_form.validate_on_submit():
        # validates if user is in database
        user = User.query.filter_by(username=login_form.username.data).first()
        
        # if user exists, verify password
        if user is not None and user.verify_password(login_form.password.data):
            # log user in
            login_user(user)
            return redirect(url_for('home.search'))
        
        # if user does not exist, give message that says its wrong
        else:
            flash('Invalid email or password.')

    return render_template('auth/login.html', form=login_form, title='Login')

@auth.route('/logout')
@login_required
def logout():
    """
    Handles requests to and from logout route form and logs a user out by using flask_login
    """

    logout_user()
    flash('You have successfully been logged out.')

    return redirect(url_for('auth.login'))
