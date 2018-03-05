from flask import (redirect,
                   render_template,
                   url_for
)
from flask_login import login_required

from . import home
from forms import SearchForm
from elasticsearch import Elasticsearch

host = "http://localhost:9200"
elastic_search = Elasticsearch(host)

@home.route('/')
def homepage():
    """
    Render the homepage template on / route
    """

    return render_template('home/index.html', title="Welcome")

@home.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    """
    Render the dashboard template on /search route
    """
    search_form = SearchForm()
    if search_form.validate_on_submit():
        return redirect((url_for('home.search_results', query=search_form.search.data)))
    return render_template('home/search.html', form=search_form ,title="Search")

@home.route('/search_results/<query>')
@login_required
def search_results(query):
    es.search(body=query)
    return render_template('home/search_results.html', query=query)
