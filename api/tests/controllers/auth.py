import logging
from requests.auth import AuthBase

from app.helpers import Token

log = logging.getLogger(__name__)

class AdminAuth(AuthBase):
    def __call__(self, request):
        # admin user is always user id 1, so we can hard code it here
        token = Token.create(data={'sub': 1}).decode('utf-8')
        request.headers['Authorization'] = 'Bearer ' + token
        return request
