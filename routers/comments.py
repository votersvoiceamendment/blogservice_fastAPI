from typing import List
from uuid import UUID
from fastapi import APIRouter, HTTPException, status
from models.comment import Comment
from schemas.comment import CommentBase

router = APIRouter(prefix="/api/v1/posts/{post_id}/comments")

@router.get("/", response_model=List[Comment])
async def get_comments(post_id: UUID):
	return ""

@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_comment(post_id: UUID, comment: CommentBase):
	return