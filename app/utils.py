from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ---------HASHING AND VERIFICATION FUNCTIONS---------


def hash(password: str):
    return pwd_context.hash(password)

def verify(plain_password: str, hashed_pass):
    return pwd_context.verify(plain_password, hashed_pass)

