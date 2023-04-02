from fastapi import FastAPI
from pydantic import BaseModel
from typing import Text,Optional
from datetime import datetime
from uuid import uuid4 as uuid

app = FastAPI()

posts=[]

#post Model
class Post(BaseModel):
    id:Optional[str]
    tittle:str
    author:str
    content:Text
    created_at:datetime=datetime.now()
    published_at:Optional[datetime]
    published:bool=False



@app.get("/")

def root():
    return {"message": "Fast API de Andres "}

@app.get("/post")
def getpost():
    return posts

@app.post("/posts")
def save_post(post:Post):
    post.id=str(uuid())
    posts.append(post.dict())
    return "received"
