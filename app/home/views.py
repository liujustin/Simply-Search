from flask import (redirect,
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
    Render the dashboard template on /search route
    """
    search_form = SearchForm()
    if search_form.validate_on_submit():
        return redirect((url_for('home.search_results', query=search_form.search.data)))
    return render_template('home/search.html', form=search_form ,title="Search")

@home.route('/search_results/<query>/')
@login_required
def search_results(query):
    page, per_page, offset = get_page_args()
    print page, per_page, offset
    result = searching_elastic.searching_elastic(query)
    current_result = result[offset:per_page*page]
    # new_result = [result[x:x+10] for x in xrange(0, len(result), 10)]
    # print new_result
    pagination = Pagination(page=page, per_page=per_page, offset=offset,
                            total=len(result), record_name='result', css_framework='foundation')
    return render_template('home/search_results.html', results=current_result, pagination=pagination, per_page=per_page)

@home.route('/search_results/<query>/<mongo_id>')
@login_required
def mongo_results(query, mongo_id):
    result = searching_mongo.searching_mongo(mongo_id)
    return render_template('home/mongo_results.html', results=result)

