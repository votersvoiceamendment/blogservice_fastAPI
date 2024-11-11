from typing import List
from fastapi import APIRouter, HTTPException, status
from ..models import Comment

router = APIRouter(prefix="/api/v1/posts/{post_id}/comments")

@router.get("/", response_model=List[Comment])
async def get_comments():
	return ""