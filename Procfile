web: FLASK_CONFIG=production
web: FLASK_APP=run.py
web: flask db init
web: flask db migrate
web: flask db upgrade
web: flask run --host=0.0.0.0 --port=${PORT}
