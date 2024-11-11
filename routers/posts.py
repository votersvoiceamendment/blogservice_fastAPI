from typing import List
from fastapi import APIRouter, HTTPException, status
from ..models import Post

router = APIRouter(prefix="/api/v1/posts")

@router.get("/", response_model=List[Post])
async def get_posts():
	return ""