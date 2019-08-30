# a root conftest.py needs to exist for pytest to properly figure out our app
# structure

# load the pytest docker compose plugin
pytest_plugins = ("docker_compose",)
