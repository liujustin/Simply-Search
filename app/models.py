from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

class User(UserMixin, db.Model):
    """
    Create a user table with email, username, firstname, lastname, password
    """

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        """
        Prevent password from being accessed
        """

        raise AttributeError('password is not a readable attribute')
    
    @password.setter
    def password(self, password):
        """
        Set hashed password
        """

        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed passwords match actual password
        """
        
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return '<User: {}>'.format(self.username)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
