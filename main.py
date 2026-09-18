from fastapi import FastAPI, Depends,HTTPException
from requests import request
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import models,schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#home
@app.get("/")
def home():
    return {"message": "Welcome to the Blog API"}

#create blog
@app.post("/blogs", response_model=schemas.BlogResponse)
def create_blog(blog: schemas.BlogCreate, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=blog.title, content=blog.content)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

#read all blogs
