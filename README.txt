This project is written by python with FastAPI and Tortoise ORM.

"main.py" is the entry point and "models.py" is the data model,
"venv" is the pre-created virtual environment.
Seed data has been built into the sqlite db: "store.db".

To run the project:

1. start the virtual environment:
. venv/bin/activate

2. run the following command:
uvicorn main:app --reload

3. The web app http://127.0.0.1:8000/
will auto redirect to the page http://127.0.0.1:8000/docs
expand each endpoint and click "Try it out" and "execute" to test the feature!
