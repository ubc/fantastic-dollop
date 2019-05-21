import logging

import os

log = logging.getLogger(__name__)

def getDbUrl():
    return "postgresql://%s:%s@%s/%s" % (
        os.getenv("DB_USER", "user"),
        os.getenv("DB_PASSWORD", "pass"),
        os.getenv("DB_HOST", "localhost"),
        os.getenv("DB_NAME", "dbname"),
    )

def getTokenSecret():
    secret = os.getenv("TOKEN_SECRET", "")
    if not secret:
        log.error("################ USING INSECURE TOKEN! ################")
        log.error("No token secret was configured in environment variables!")
        log.error("Generated session tokens will NOT be secure.")
        secret = "2cbb8578e52fe815cff03e2d61b93ee1801905c1b36af7c25995b3ca6d0e5129"
    return secret

def getTokenAlgorithm():
    algorithm = os.getenv("TOKEN_ALGORITHM", "HS256")
    return algorithm

def getTokenExpire():
    expire = os.getenv("TOKEN_EXPIRE_MINUTES", "180")
    expire = int(expire)
    return expire
