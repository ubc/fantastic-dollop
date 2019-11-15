## Add new migration file
In the api root, you can run alembic to generate a new migration file:

    PYTHONPATH=. alembic revision -m "MIGRATION MESSAGE"

Note that we're adding the api root to the python path because some migrations require imports from the app package.
