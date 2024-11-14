
from typing import Optional, List
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class CommentBase(BaseModel):
	text: str

class Comment(CommentBase):
	id: UUID
	post_id: UUID
	vva_user_id: str
	created_at: datetime
	updated_at: datetime

	class Config:
		from_attributes = True
