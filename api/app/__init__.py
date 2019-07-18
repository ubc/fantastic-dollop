import databases
from app.config import EnvConfig
from depot.manager import DepotManager

db = databases.Database(EnvConfig.getDbUrl())

# initialize file depot
DepotManager.configure('default', {
    'depot.storage_path': './uploaded_files'
})
