from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import models
from .database import engine, get_db
from .routers import post, user, auth, vote


# -------------APP-------------

app = FastAPI()

# Allow domains to talk to our API
# "*" means all domains
# "https://www.google.com" allows people from google.com to fetch data from our API
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------sqlalchemy - Database create from models file-------------

# models.Base.metadata.create_all(bind=engine)

# --- We do not need this anymore since we are using alembic to auto generate

# -------------ROOT-------------

@app.get("/")
async def root(db:Session = Depends(get_db)):
    return {"message" : "Welcome to my API"}

# -------------ROUTERS-------------

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


