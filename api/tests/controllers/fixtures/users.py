import logging
import string
import random
import pytest

# can't be helped, need the table spec because sqlalchemy doesn't give you# anything back if you just do a raw sql insert, very annoying. If we do
# the insert with a table spec, it'll give us at least the id inserted
from app.tables import UserTable

log = logging.getLogger(__name__)

@pytest.fixture
def add_tmp_user(dbconn):
    """ Create a temporary user for use in a test case.
    This user will be deleted at the end of the test function.
    """
    # random username
    # password is 'password' hashed
    user = {
        'username': ''.join(random.choices(string.ascii_uppercase + string.digits, k=8)),
        'password': '$2b$12$Y9NJzzwbOrAFay/.Z0Cy6O4ryoBOG5vWgfro0iQisljYvjCEXJcMa'
    }
    query = UserTable.table.insert().values(
        username=user['username'], password=user['password'])
    result = dbconn.execute(query)
    user['id'] = result.inserted_primary_key[0]
    yield user # let test function execute
    # cleanup after test function finish
    query = UserTable.table.delete().where(
        UserTable.table.c.id == user['id'])
    dbconn.execute(query)
