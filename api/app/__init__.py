import databases
from app.config import EnvConfig

db = databases.Database(EnvConfig.getDbUrl())

