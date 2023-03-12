from datetime import datetime
import os 

from fastapi import APIRouter,HTTPException,status

import posts.api.v1.crud as crud
import posts.api.v1.schema as schema


api_router = APIRouter()

@api_router.get("/post/{post_uuid}")
def get_post(post_uuid: str) -> schema.Post:
    post = crud.read_post(post_uuid)
    if not post:
        raise HTTPException()
    
    return post

@api_router.get("/post/{post_uuid}/reactions")
def get_reactions(post_uuid: str) -> schema.Reaction:
    reactions = crud.read_reactions(post_uuid)

    return reactions

@api_router.post("/post/")
def post_new_post(request_body: schema.NewPost):
    post = schema.NewPost(
        title = request_body.title,
        tags = request_body.tags,
        website = request_body.website,
        location = request_body.location,
        since = request_body.since,
        image = request_body.image,
        body = request_body.body,        
    )
    user = get_current_user()  #たぶんこういうこと
    crud.create_new_post(post,user)

    return status.HTTP_201_CREATED


