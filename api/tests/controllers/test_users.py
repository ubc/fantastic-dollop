import logging

import pytest

from starlette.testclient import TestClient

from app import main
from app.config import EnvConfig

from .auth import AdminAuth

TOKEN_SECRET = EnvConfig.getTokenSecret()
TOKEN_ALGORITHM = EnvConfig.getTokenAlgorithm()

log = logging.getLogger(__name__)

@pytest.mark.usefixtures('reset_database')
class TestUsers:
    def test_list_users(self):
        with TestClient(main.app) as client:
            # non-signed-in users don't have access
            response = client.get('/users')
            assert response.status_code == 401
            # admins have access
            response = client.get('/users', auth=AdminAuth())
            assert response.status_code == 200
            assert type(response.json()) is list
            assert len(response.json()) == 1
            user = response.json()[0]
            assert user['id'] == 1
            assert user['username'] == 'admin'
            assert user['isAdmin'] is True

    def test_get_single_user(self):
        with TestClient(main.app) as client:
            # non-signed-in users don't have access
            response = client.get('/users/1')
            assert response.status_code == 401
            # admins have access
            response = client.get('/users/1', auth=AdminAuth())
            assert response.status_code == 200
            user = response.json()
            assert user['id'] == 1
            assert user['username'] == 'admin'
            assert user['isAdmin'] is True

    def test_add_user(self, dbconn):
        with TestClient(main.app) as client:
            # non-signed-in users don't have access
            expectedUser = {'username': 'user1', 'password': 'blah'}
            response = client.post('/users', json=expectedUser)
            assert response.status_code == 401
            # admins have access
            response = client.post('/users', json=expectedUser, auth=AdminAuth())
            assert response.status_code == 201
            actualUser = response.json()
            assert expectedUser['username'] == actualUser['username']
            # make sure changes are actually in the database
            query = 'SELECT * FROM "user" WHERE id = ' + str(actualUser['id'])
            result = dbconn.execute(query)
            result = result.fetchone()
            assert expectedUser['username'] == result['username']

    def test_edit_user(self, add_tmp_user, dbconn):
        with TestClient(main.app) as client:
            expectedUser = add_tmp_user
            expectedUser['name'] = 'First Last'
            # non-signed-in users don't have access
            userId = str(expectedUser['id'])
            response = client.post('/users/'+userId, json=expectedUser)
            assert response.status_code == 401
            # admins have access
            response = client.post('/users/'+userId, json=expectedUser,
                                   auth=AdminAuth())
            assert response.status_code == 200
            actualUser = response.json()
            assert expectedUser['username'] == actualUser['username']
            assert expectedUser['name'] == actualUser['name']
            # make sure changes are actually in the database
            query = 'SELECT * FROM "user" WHERE id = ' + str(actualUser['id'])
            result = dbconn.execute(query)
            result = result.fetchone()
            assert expectedUser['username'] == result['username']
            assert expectedUser['name'] == result['name']

    def test_delete(self, add_tmp_user, dbconn):
        with TestClient(main.app) as client:
            # non-signed-in users should be rejected
            response = client.delete('/users/1')
            assert response.status_code == 401
            # admin should be able to successfully delete user
            userId = add_tmp_user['id']
            response = client.delete('/users/' + str(userId), auth=AdminAuth())
            assert response.status_code == 204
            # make sure user was actually deleted
            query = 'SELECT * FROM "user" WHERE id = ' + str(userId)
            result = dbconn.execute(query).first()
            assert result is None
