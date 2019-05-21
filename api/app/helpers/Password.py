from passlib.context import CryptContext

context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify(plain, hashed):
    return context.verify(plain, hashed)

def hash(password: str):
    return context.hash(password)
