from typing import List, Dict, Any
from uuid import UUID
from fastapi import APIRouter, HTTPException, status, Depends
from auth.jwt import JWT
from sqlalchemy.orm import Session
from crud import post
from crud.post import add_post, get_all_posts, get_post_by_id, update_post_by_id
from database import get_db
from schemas.post import PostBase, Post
from auth.security import get_current_user, check_role
from constants.roles import ROLE

router = APIRouter(prefix="/api/v1/posts")

@router.get("/", response_model=List[Post])
async def get_posts(db: Session = Depends(get_db)):
	return get_all_posts(db=db)

@router.get("/ids", response_model=List[UUID], dependencies=[Depends(check_role([ROLE.ADMIN]))])
async def get_post_ids(current_user: JWT = Depends(get_current_user)):
	user_id = current_user.user_id
	roles = current_user.roles
	return []

@router.get("/{id}", response_model=Post)
async def get_post(id: UUID, db: Session = Depends(get_db)):
	return get_post_by_id(db=db, id=id)

@router.post("/", status_code=status.HTTP_201_CREATED, dependencies=[Depends(check_role([ROLE.ADMIN]))])
async def create_post(
	post: PostBase, 
	current_user: JWT = Depends(get_current_user),
	db: Session = Depends(get_db)
):
	user_id = current_user.user_id
	add_post(db=db, post=post, user_id=user_id)
	return


@router.put("/{id}", status_code=status.HTTP_200_OK, dependencies=[Depends(check_role([ROLE.ADMIN]))])
async def update_post(
	id: UUID, 
	updated_post: PostBase, 
	db: Session = Depends(get_db)
):
	update_post_by_id(db=db, post_id=id, updated_post=updated_post)
	return