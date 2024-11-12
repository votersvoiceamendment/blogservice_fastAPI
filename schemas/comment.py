
from typing import Optional, List
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from comment import Comment

class CommentCreate(BaseModel):
	post_id: UUID
	text: str

class Comment(CommentCreate):
	id: UUID
	vva_user_id: str
	created_at: datetime
	updated_at: datetime

	class Config:
		from_attributes = True
