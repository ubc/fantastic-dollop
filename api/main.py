from fastapi import FastAPI

import logging
import logging.config
import os
import yaml # for reading the logging config file

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

logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/")
async def root():
    logger.debug("HELLO WORLD 1")
    return {"message": "Hello World"}
