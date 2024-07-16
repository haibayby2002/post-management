from fastapi import FastAPI, status, HTTPException, Response
from fastapi.params import Depends
from .database import SessionLocal, engine
from . import schema
from sqlalchemy.orm import Session
# import utils

from . import models
from .database import engine
from .routers import post, user, auth



models.Base.metadata.create_all(bind=engine)


# Dependency

app = FastAPI()
POSTS = [
    {'id': '1', 'title': 'title 1', 'content': 'content 1'},
    {'id': '2', 'title': 'title 2', 'content': 'content 2'},
    {'id': '3', 'title': 'title 3', 'content': 'content 3'}
]

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}




