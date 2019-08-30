import logging
import os
import subprocess
from time import time, sleep

import psycopg2
import sqlalchemy as sa

import pytest

from app.config import EnvConfig

log = logging.getLogger(__name__)

dbUrl = EnvConfig.getDbUrl()

# spins up the postgres docker image, we only do this once per session,
# wait for the postgres container to be ready to accept connections
@pytest.fixture(scope='session')
def wait_for_pg(session_scoped_container_getter):
    # can configure timeout intervals with env vars if needed
    check_timeout = os.getenv('POSTGRES_CHECK_TIMEOUT', 30)
    check_interval = os.getenv('POSTGRES_CHECK_INTERVAL', 1)
    interval_unit = 'second' if check_interval == 1 else 'seconds'

    start_time = time()
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())
    assert check_timeout > 0
    assert check_interval < check_timeout
    while time() - start_time < check_timeout:
        try:
            conn = psycopg2.connect(dbUrl)
            logger.info('Postgres is ready! ✨ 💅')
            conn.close()
            return True
        except psycopg2.OperationalError:
            logger.info(f'Postgres isn\'t ready. Waiting for {check_interval} {interval_unit}...')
            sleep(check_interval)

    logger.error(f'We could not connect to Postgres within {check_timeout} seconds.')
    return False


# load data into postgres, this is executed at the module level, so every
# test file will start with a new database
@pytest.fixture(scope='module')
def reset_database(wait_for_pg):
    engine = sa.create_engine(dbUrl)
    conn = engine.connect()
    conn.execute("select 'drop table \"' || tablename || '\" cascade;' from pg_tables where schemaname = 'public';")
    subprocess.run(['alembic', 'upgrade', 'head'])

