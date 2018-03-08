from flask import (
    redirect,
    render_template,
    url_for
)
from flask_login import login_required
from flask_paginate import Pagination, get_page_args
from . import home
from forms import SearchForm
from ..search import searching_elastic, searching_mongo

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
    Render the dashboard template on /search route after logging in
    """
    search_form = SearchForm()
    if search_form.validate_on_submit():
        return redirect((url_for('home.search_results', query=search_form.search.data)))
    return render_template('home/search.html', form=search_form ,title="Search")

@home.route('/search_results/<query>/')
@login_required
def search_results(query):
    """
    Render the search results template on /search_results/<query> and chooses how many results
    to display per page using Pagination
    """
    page, per_page, offset = get_page_args()
    search_result = searching_elastic.searching_elastic(query)
    # array that will only display a couple of results per page depending on the offset
    page_result = search_result[offset:per_page*page]
    pagination = Pagination(page=page, per_page=per_page, offset=offset,
                            total=len(search_result), record_name='page_result', css_framework='foundation')
    return render_template('home/search_results.html', results=page_result, pagination=pagination, per_page=per_page)

@home.route('/search_results/<query>/<mongo_id>')
@login_required
def mongo_results(query, mongo_id):
    """
    After clicking on a page in the search results template, render mongo results template
    to show the data from the mongodb that matches the id returned from elastic.
    """
    result = searching_mongo.searching_mongo(mongo_id)
    return render_template('home/mongo_results.html', results=result)

