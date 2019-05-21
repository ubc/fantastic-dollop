from sqlalchemy import MetaData

# sqlalchemy use this to store a description of the database, so we need to share
# the same instance among all tables
dbMetadata = MetaData()
