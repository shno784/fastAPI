from typing import Optional
from pydantic import BaseModel, EmailStr, conint
from datetime import datetime


#Scheme for when user creates an account
class CreateUser(BaseModel):
    email: EmailStr
    password: str

#Scheme for any info to send back to the user
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str
#Pydantic to filter info and schema
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

#passing Postbase in by default will give any class the values of postBase
class CreatePost(PostBase):
    pass #accepts whatever, currently they're both the same


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)

    
#scheme for when someone posts a post, uses  postbase as the main so you
#already have title published and content
class PostResponse(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserResponse

    class Config:
        orm_mode = True

class PostVote(BaseModel):
    Post: PostResponse
    votes: int

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None
