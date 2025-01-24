from .. import models, schemas, utils
from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List

# -------------TAGS HELP WITH DOCUMENTATION OF FASTAPI-------------
# -------------PREFIX IS FOR NOT REPEATING "/USERS"-------------

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

# -------------USER STUFF-------------

# -------------CREATE-------------

@router.post("/", status_code=status.HTTP_201_CREATED,response_model=schemas.UserOut)
async def create_user(user: schemas.UserCreate, db:Session = Depends(get_db)):

    # hash the password
    hashed_pass = utils.hash(user.password)
    user.password = hashed_pass

    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# -------------READ-------------

@router.get("/{id}")
async def get_user(id: int, response: Response, db:Session = Depends(get_db), response_model=schemas.UserOut):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id: {id} was not found")
    return user

@router.get("/test")
async def get_user(response: Response, db:Session = Depends(get_db), response_model=schemas.UserOut):
    user = db.query(models.User).filter(models.User.id == 1).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user was not found")
    return user
