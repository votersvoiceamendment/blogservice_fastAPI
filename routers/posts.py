from typing import List
from uuid import UUID
from fastapi import APIRouter, HTTPException, status
from schemas.post import PostBase, Post

router = APIRouter(prefix="/api/v1/posts")

@router.get("/", response_model=List[Post])
async def get_posts():
	return []

@router.get("/ids", response_model=List[UUID])
async def get_post_ids():
	return []

# @router.get("/{id}", response_model=Post)
# async def get_post():
# 	return 

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_post(post: PostBase):
	print(post)
	return

@router.put("/{id}", status_code=status.HTTP_200_OK)
async def update_post(id: UUID, updated_post: PostBase):
	return