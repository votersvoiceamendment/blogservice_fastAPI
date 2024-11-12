from typing import Optional, List
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class PostBase(BaseModel):
	title: str
	text: str
	featured: Optional[bool] = False


class Post(PostBase):
	id: UUID
	vva_user_id: str
	created_at: datetime
	updated_at: datetime

	class Config:
		from_attributes = True