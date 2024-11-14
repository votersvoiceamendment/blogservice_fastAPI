from typing import List, Dict, Any
from uuid import UUID
from fastapi import APIRouter, HTTPException, status, Depends
from auth.jwt import JWT
from crud.comment import add_comment_to_post, get_comments_for_post
from crud.post import get_post_by_id
from schemas.comment import CommentBase, Comment
from auth.security import get_current_user, check_role
from constants.roles import ROLE
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter(prefix="/api/v1/posts/{post_id}/comments")

@router.get("/", response_model=List[Comment])
async def get_comments(post_id: UUID, db: Session = Depends(get_db)):
	return get_comments_for_post(db=db, post_id=post_id)

@router.post("/", status_code=status.HTTP_201_CREATED, dependencies=[Depends(check_role([ROLE.USER]))])
async def add_comment(
	post_id: UUID, 
	comment: CommentBase, 
	current_user: JWT = Depends(get_current_user),
	db: Session = Depends(get_db)
):
	add_comment_to_post(
		db=db,
		user_id=current_user.user_id,
		post_id=post_id,
		comment=comment
    )
	return