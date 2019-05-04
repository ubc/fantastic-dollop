from sqlalchemy.ext.declarative import declarative_base

# sqlalchemy docs says there's usually just one instance of this base class
# declaring it here so all models can use it
SQLAlchemyBase = declarative_base()
