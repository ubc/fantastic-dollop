# request body data validation
from pydantic import BaseModel

# For data validation with incoming and outgoing data, this base class contains
# fields that are in both requests and responses.
# unfortunately, this mechanism suffers from code duplication with the database 
# table definition, no clue how to address that
class UserBase(BaseModel):
    username: str
    name: str = None
    preferredName: str = None
    email: str = None
    studentNumber: str = None


# Incoming request data will need to match this spec.
class UserIn(UserBase):
    password: str

# Outgoing response data will be filtered to match this spec.
class UserOut(UserBase):
    id: int
