import logging

from passlib.context import CryptContext

log = logging.getLogger(__name__)

context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify(plain, hashed):
    try:
        return context.verify(plain, hashed)
    except ValueError as e:
        log.error("Password hash format error: " + str(e))
        return False

def hash(password: str):
    return context.hash(password)
