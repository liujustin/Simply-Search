# Search Me

A basic web application utilizing the Flask framework with Jinja2 templating in order to allow for custom searching. The application allows for registering, authorization and searching.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What you need to have before being able to use this project.

* [Python 2.7](https://www.python.org)
* [Flask](http://flask.pocoo.org)
* [Virtualenv](https://virtualenv.pypa.io/)
* [Virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/)
* [MySQL](https://www.mysql.com)

### Installing

A step by step series of examples that tell you have to get a development env running

To get started, open a terminal window and run the following commands:

```bash
pip install virtualenv

pip install virtualenvwrapper

mkvirtualenv searchme

pip install -r requirements.txt
```

After doing all this, you should now have all the requirements listed in requirements.txt.

Now, you'll want to set some environment variables to get started:

```bash
export FLASK_CONFIG=development
export FLASK_APP=run.py
```

You'll also want to set up additional environment variables for Mongo, SQLALCHEMY and Secret Keys:

* For ELASTIC_HOSTS, use
```bash
export ELASTIC_HOSTS=[{ "host" : "localhost", "port" : 9200 }]
```

or replace with your own host link (maybe using [Bonsai](https://bonsai.io/index.html) that is in a list format

* For MONGO_URI, use 

```bash
export MONGO_URI='mongodb://localhost:27017'
```

or replace with your own host link (maybe using [MLabs](https://mlab.com)

* For SQLALCHEMY_DATABASE_URI, you can either set it up using MySQL

```bash
export SQLALCHEMY_DATABASE_URI=mysql://example_admin:example_password@localhost/searchme
```

or use a postgres URL made from AWS

* For WTF_CSRF_SECRET_KEY and SECRET_KEY, just create your own

```bash
export WTF_CSRF_SECRET_KEY='secretcsrfkey
export SECRET_KEY='a super secret key'
```

After this, you want to initialize your database and have migrations.

```bash
flask db init
flask db migrate
flask db upgrade
```

Now run the application:

```bash
flask run
```

## Built With

* [Python 2.7](https://www.python.org)
* [Flask](http://flask.pocoo.org)
* [Virtualenv](https://virtualenv.pypa.io/)
* [Virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/)
* [MySQL](https://www.mysql.com)
* [ElasticSearch](https://github.com/elastic/elasticsearch-py)
* [MongoDB](https://www.mongodb.com)

## Versioning

I used [Git](https://git-scm.com) for versioning. Everything was pushed to [GitHub](https://github.com) 

## Authors

* **Justin Liu** - [LinkedIn](https://www.linkedin.com/in/imjustliu/)  [GitHub](https://github.com/liujustin)

## Features:
- [X] Register a user with a username, First name, Last name, email, and 
password. 
- [X] Save the user data in MySQL database 
- [X] Login user (Validate the user information: username and password from 
MySQL). Make sure you use ORM to insert and query data in MySQL (Eg: SQLAlchemy) 
- [X] After user logs in, display a keyword search box. (Something like 
Google Search Box) 

- [X] In the backend, Add data(any type of data) in MongoDB as well as index 
the data in ElasticSearch. Make sure both the MongoDB and ES have the 
same data with same "_id" for every document (dump the data manually 
Eg. Calendar events data, flight data, etc.) 

- [X] Display search results from Elastic Search with pagination when a 
keyword search is made 
- [X] When a user clicks on any item from the search results a new tab 
should be opened to display the item details from MongoDB 
