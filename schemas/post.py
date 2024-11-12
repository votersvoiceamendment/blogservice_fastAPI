from typing import Optional, List
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class PostCreate(BaseModel):
	title: str
	text: str
	featured: Optional[bool] = False


class Post(PostCreate):
	id: UUID
	vva_user_id: str
	created_at: datetime
	updated_at: datetime

	class Config:
		from_attributes = True