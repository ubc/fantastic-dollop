import logging

import pytest

from starlette.testclient import TestClient

import jwt

from app import main
from app.config import EnvConfig


TOKEN_SECRET = EnvConfig.getTokenSecret()
TOKEN_ALGORITHM = EnvConfig.getTokenAlgorithm()

log = logging.getLogger(__name__)

@pytest.mark.usefixtures('reset_database')
class TestSignIn:
    def test_sign_in_success(self):
        with TestClient(main.app) as client:
            data = {'username': 'admin', 'password': 'admin'}
            response = client.post('/signin', data=data)
            assert response.status_code == 200
            ret = response.json()
            assert 'token_type' in ret
            assert ret['token_type'] == 'bearer'
            assert 'access_token' in ret
            # if we can decode the access token, then it's a valid token
            payload = jwt.decode(ret['access_token'], TOKEN_SECRET,
                                 algorithms=[TOKEN_ALGORITHM])
            userId: int = payload.get("sub")
            assert userId == 1

    def test_sign_in_wrong_username(self):
        with TestClient(main.app) as client:
            data = {'username': 'admin1', 'password': 'admin'}
            response = client.post('/signin', data=data)
            assert response.status_code == 400

    def test_sign_in_wrong_password(self):
        with TestClient(main.app) as client:
            data = {'username': 'admin', 'password': 'admin1'}
            response = client.post('/signin', data=data)
            assert response.status_code == 400
