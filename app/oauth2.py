from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from . import schemas, database, models
from fastapi import status, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .config import settings

# -------AUTHORISATION file for OAuth2--------

oath2_scheme = OAuth2PasswordBearer(tokenUrl="login")

#secretkey
SECRET_KEY = settings.secret_key
#algorithm
ALGORYTHM = settings.algorithm
#expiration time
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

#makes the token
def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORYTHM)

    return encoded_token

#verifies the token and token data
def verify_access_token(token: str, creds_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORYTHM])

        id: str = str(payload.get("user_id"))
        if id is None:
            raise creds_exception
        token_data = schemas.TokenData(id=id)

    except JWTError:
        raise creds_exception
    
    return token_data
    
# verifies automatically the user with the token
def get_current_user(token:str = Depends(oath2_scheme), db: Session = Depends(database.get_db)):
    creds_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})

    token = verify_access_token(token, creds_exception=creds_exception)

    user = db.query(models.User).filter(models.User.id == token.id).first()
    return user