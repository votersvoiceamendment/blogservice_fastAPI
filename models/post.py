from sqlalchemy import Column, String, Text, Boolean, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from database import Base
from uuid import uuid4
from datetime import datetime
import pytz

class Post(Base):
    __tablename__ = "post"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    vva_user_id = Column(String(36), nullable=False)
    title = Column(String(500), nullable=False)
    text = Column(Text, nullable=False)
    featured = Column(Boolean, nullable=False, default=False)
    
	# Timestamps
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(pytz.UTC), nullable=False)
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(pytz.UTC), onupdate=func.now(), nullable=False)
    
	# Relationship to comments (One-to-Many)
    comments = relationship("Comment", back_populates="post", cascade="all, delete-orphan")


# TODO FOR RETRIEVING THE TIMEZONE!!
# # Assuming `post.created_at` is a timezone-aware datetime in UTC
# user_timezone = pytz.timezone("America/New_York")  # Example user timezone
# local_time = post.created_at.astimezone(user_timezone)
# print(local_time)  # This will display the time converted to the user's timezone