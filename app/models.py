from .database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text, ForeignKey
import psycopg2
from sqlalchemy.orm import relationship

# -------------------THIS MAKES THE TABLES USING SQLALCHEMY OR ALEMBIC-------------------
# ----------it is important to have a specific structure for our API---------

class User(Base):
    __tablename__ = "users"

    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False, unique=True)
    id = Column(Integer,primary_key=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer,primary_key=True,nullable=False)
    title = Column(String,nullable=False)
    content = Column(String,nullable=False)
    published = Column(Boolean, server_default='TRUE')
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)

    owner = relationship("User")

class Votes(Base):
    __tablename__ = "votes"

    user_id = Column(Integer,ForeignKey("users.id", ondelete="CASCADE"),primary_key=True)
    post_id = Column(Integer,ForeignKey("posts.id", ondelete="CASCADE"),primary_key=True)
