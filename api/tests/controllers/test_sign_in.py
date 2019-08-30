import logging

import pytest

from starlette.testclient import TestClient

import jwt

from app import main
from app.config import EnvConfig


TOKEN_SECRET = EnvConfig.getTokenSecret()
TOKEN_ALGORITHM = EnvConfig.getTokenAlgorithm()

log = logging.getLogger(__name__)

@pytest.mark.usefixtures('wait_for_pg', 'reset_database')
class TestSignIn:
    def test_sign_in_success(self, caplog):
        with TestClient(main.app) as client:
            data = {'username': 'admin', 'password': 'admin'}
            response = client.post('/signin', data=data)
            assert response.status_code == 200
            caplog.clear()
            caplog.set_level(logging.DEBUG)
            log.debug(response.json())
            ret = response.json()
            assert 'token_type' in ret
            assert ret['token_type'] == 'bearer'
            assert 'access_token' in ret
            # if we can decode the access token, then it's a valid token
            payload = jwt.decode(ret['access_token'], TOKEN_SECRET,
                                 algorithms=[TOKEN_ALGORITHM])
            userId: int = payload.get("sub")
            assert userId == 1

    def test_sign_in_wrong_user(self):
        with TestClient(main.app) as client:
            data = {'username': 'admin1', 'password': 'admin'}
            response = client.post('/signin', data=data)
            assert response.status_code == 400

    def test_sign_in_wrong_password(self):
        with TestClient(main.app) as client:
            data = {'username': 'admin', 'password': 'admin1'}
            response = client.post('/signin', data=data)
            assert response.status_code == 400


