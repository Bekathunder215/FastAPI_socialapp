from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

#-----------SCHEMAS FOR OUR DATA WITH PYDANTIC----------

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: Optional[datetime]

    class Config:
        from_attributes = True


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    created_at: datetime
    user_id: int
    owner: UserOut

    class Config:
        from_attributes = True

class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None
    # token_type: str

class Vote(BaseModel):
    post_id: int
    dir: bool