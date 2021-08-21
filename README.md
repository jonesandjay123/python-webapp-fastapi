### The project is made by python with FastAPI and Tortoise ORM. ###

`main.py` is the entry point and `models.py` is the data model,
seed data has been added into the sqlite db: `store.db` in advance.


To run the project, please do the follow steps:

1. `cd` to the project directory that you've just downloaded
(if you have both python 2 and 3, run `alias python=python3`)

2. run `python3 -m venv venv` and then `. venv/bin/activate` to start the virtual environment

3. `python3 -m pip install -r requirements.txt` to install all the requirement.

4. finally run the the command below to start the app:
`uvicorn main:app --reload`

The web app [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
will auto redirect to the page [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
expand each endpoint and click "Try it out" and "execute" to test the feature!
