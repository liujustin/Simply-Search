from flask import render_template
from flask_login import login_required

from . import home


@home.route('/')
def homepage():
    """
    Render the homepage template on / route
    """

    return render_template('home/index.html', title="Welcome")

@home.route('/search')
@login_required
def search():
    """
    Render the dashboard template on /search route
    """

    return render_template('home/search.html', title="Search")
