
from typing import Optional, List
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from comment import Comment

class CommentCreate(BaseModel):
	post_id: UUID
	vva_user_id: str
	text: str

class Comment(CommentCreate):
	id: UUID
	created_at: datetime
	updated_at: datetime

	class Config:
		orm_mode = True
