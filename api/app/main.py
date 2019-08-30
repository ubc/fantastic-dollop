import logging
import logging.config
import os
import yaml # for reading the logging config file

from fastapi import FastAPI
from app.controllers import Users
from app.controllers import SignIn
from app.controllers import Courses
from app.controllers import Enrolments
from app.controllers import Roles
from app import db

# Configures logging for the whole app, will default to using the settings
# in `config/logging.yml` which will set logging at DEBUG to stdout. The config
# file path can be overridden with the environment variable `LOG_CONFIG`.
configPath = "config/logging.yml"
envConfigPath = os.getenv("LOG_CONFIG", None)
if envConfigPath:
    configPath = envConfigPath
if os.path.exists(configPath):
    with open(configPath, 'rt') as f:
        config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)
else:
    logging.basicConfig(level=logging.DEBUG)

log = logging.getLogger(__name__)

app = FastAPI()

app.include_router(Courses.router)
app.include_router(Users.router)
app.include_router(SignIn.router)
app.include_router(Enrolments.router)
app.include_router(Roles.router)

# clean up database connection
@app.on_event("startup")
async def startup():
    await db.connect()

@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()
