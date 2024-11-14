from typing import List, Dict, Any
from uuid import UUID
from fastapi import APIRouter, HTTPException, status, Depends
from auth.jwt import JWT
from schemas.comment import CommentBase, Comment
from auth.security import get_current_user, check_role
from constants.roles import ROLE

router = APIRouter(prefix="/api/v1/posts/{post_id}/comments")

@router.get("/", response_model=List[Comment])
async def get_comments(post_id: UUID):
	return []

@router.post("/", status_code=status.HTTP_201_CREATED, dependencies=[Depends(check_role([ROLE.USER]))])
async def add_comment(post_id: UUID, comment: CommentBase, current_user: JWT = Depends(get_current_user)):
	user_id = current_user.user_id
	roles = current_user.roles
	print(post_id, comment, user_id, roles)
	return