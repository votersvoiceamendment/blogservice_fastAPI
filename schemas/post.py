from typing import Optional, List
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from comment import Comment


class PostCreate(BaseModel):
	vva_user_id: str
	title: str
	text: str
	featured: Optional[bool] = False


class Post(PostCreate):
	id: UUID
	created_at: datetime
	updated_at: datetime

	class Config:
		orm_mode = True