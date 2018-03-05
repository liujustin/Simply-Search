# EnerKnol Challenge
## To get started, you must have:
- Python 2.7
- Flask
- Virtualenv
- MySQL
## Then install dependencies
```bash
pip install -r requirements.txt
```
After this, make sure you have launched your MySQL database and have it running.

## To run the program:

```bash
flask run
````

## Requirements:
- [ ] Register a user with a username, First name, Last name, email, and 
password. 
- [ ] Save the user data in MySQL database 
- [ ] Login user (Validate the user information: username and password from 
MySQL). Make sure you use ORM to insert and query data in MySQL (Eg: SQLAlchemy) 
- [ ] After user logs in, display a keyword search box. (Something like 
Google Search Box) 

- [ ] In the backend, Add data(any type of data) in MongoDB as well as index 
the data in ElasticSearch. Make sure both the MongoDB and ES have the 
same data with same "_id" for every document (dump the data manually 
Eg. Calendar events data, flight data, etc.) 

- [ ] Display search results from Elastic Search with pagination when a 
keyword search is made 
- [ ] When a user clicks on any item from the search results a new tab 
should be opened to display the item details from MongoDB 
