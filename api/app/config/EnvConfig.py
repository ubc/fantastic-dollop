import os

def getDbUrl():
    return "postgresql://%s:%s@%s/%s" % (
        os.getenv("DB_USER", "user"),
        os.getenv("DB_PASSWORD", "pass"),
        os.getenv("DB_HOST", "localhost"),
        os.getenv("DB_NAME", "dbname"),
    )

