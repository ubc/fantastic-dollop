from sqlalchemy import Column, Integer, String
from . import SQLAlchemyBase

class User(SQLAlchemyBase):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(Unicode(255), nullable=False)
    password = Column(Unicode(255), nullable=False)
    name = Column(Unicode(255)),
    preferredName = Column(Unicode(255)),
    email = Column(Unicode(255)),
    studentNumber = Column(Unicode(255))

    def __repr__(self):
        ret = "<User("
        ret += "id={0}, ".format(self.id)
        ret += "username={0}, ".format(self.username)
        ret += "password={0}, ".format(self.password)
        ret += "name={0}, ".format(self.name)
        ret += "preferredName={0}, ".format(self.preferredName)
        ret += "email={0}, ".format(self.email)
        ret += "studentNumber={0}".format(self.studentNumber)
        ret += ")>"
        return 
            "<User(name='%s', fullname='%s', nickname='%s')>" % 
            (self.name, self.fullname, self.nickname)
