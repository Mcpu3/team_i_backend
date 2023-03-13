from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    user_uuid: str
    user_name: str
    display_name: Optional[str]
    created_at: datetime
    updated_at: Optional[datetime]


class PrivateUser(User):
    hashed_password: str
    deleted: bool

class Post(BaseModel):
    post_uuid: str
    user_uuid: str
    title: str
    summary: Optional[str]
    tags_uuid: Optional[List[str]]
    website: Optional[str]
    location_uuid: Optional[str]
    since: Optional[str]
    image_uuid: Optional[str]
    body: str
    created_at: datetime
    updated_at: Optional[datetime]

class NewPost(BaseModel):
    title: str
    tags: Optional[List[str]]
    website: Optional[str]
    location: Optional[str]
    since: Optional[str]
    image: Optional[str]
    body: str

class Tag(BaseModel):
    tag_uuid: str
    body: str
    created_at: datetime
    updated_at: Optional[datetime]

class Location(BaseModel):
    location_uuid: str
    body: str
    created_at: datetime
    updated_at: Optional[datetime]

class Image(BaseModel):
    image_uuid: str
    user_uuid: str
    body: str
    created_at: datetime
    updated_at: Optional[datetime]

class Reaction(BaseModel):
    like: int
    super_like: int
