from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    """
    Form for users to search in a string text box with a submit field.
    """
    search = StringField('', validators=[DataRequired()])
    submit = SubmitField('Search')
