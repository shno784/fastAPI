
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas, utils, oauth2
from typing import List, Optional
from ..database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import func

#So we don't have to write /posts all the time 
#tag is to group the requests
router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)
#Get all posts
@router.get("/",response_model=List[schemas.PostVote])
def get_post(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user),
limit: int = 10, skip: int = 0, search: Optional[str] = ""):

    # posts_query = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

    posts = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id,isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    return posts


#Get a single post
@router.get("/{id}", response_model=schemas.PostVote)
def get_post(id: int, response: Response, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    #post = db.query(models.Post).filter(models.Post.id == id).first()
    post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id,isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()
    #Change status Code
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} is not Found.")

    return post

#Create a post
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.PostResponse)
#define the post class ad newpost and print it out   user_id to make sure you have to be logged in to do it 
def create_post(post: schemas.CreatePost, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
   # new_post = models.Post(title = post.title, content = post.content, published = post.published)
    new_post = models.Post(owner_id = current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

# we can just use post.dict() and then **post.dict() to unpack it form a dictionary into a  regular typp


#Delete Post
@router.delete("/{id}")
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    #Logic to find all posts based on ID
    post_query = db.query(models.Post).filter(models.Post.id == id)
    #Grabs the first post that matches with the ID
    post_to_delete = post_query.first()

    if post_to_delete == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} does not exist.")

    if post_to_delete.owner_id != current_user.id:

        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorized to perform requested action.")

    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
    

#Update post
@router.put("/{id}", response_model=schemas.PostResponse)
def update_post(id: int, post: schemas.CreatePost, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    #Logic to find all posts based on ID
    post_query = db.query(models.Post).filter(models.Post.id == id)
    #Grabs the first post that matches with the ID
    post_to_udpdate = post_query.first()


    if post_to_udpdate == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} does not exist.")

    if post_to_udpdate.owner_id != current_user.id:

        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorized to perform requested action.")
    
    post_query.update(post.dict(),synchronize_session=False)
    db.commit()

    return post_query.first()