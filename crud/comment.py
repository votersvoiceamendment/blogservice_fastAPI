from fastapi import HTTPException, status
from typing import List
from uuid import UUID
from sqlalchemy.orm import Session

from models.post import Post
from models.comment import Comment
from schemas.comment import CommentBase

def get_comments_for_post(db: Session, post_id: UUID) -> List[Comment]:
    # Check if the post exists
    # If not raise an exception
    post: Post = db.query(Post).filter(Post.id == post_id).first()
    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found"
        )
    
    return db.query(Comment).filter(Comment.post_id == post_id).order_by(Comment.created_at.desc()).all()

def add_comment_to_post(db: Session, user_id: UUID, post_id: UUID, comment: CommentBase):
    # Check if the post exists
    # If not raise an exception
    post: Post = db.query(Post).filter(Post.id == post_id).first()
    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found"
        )
    # Make the new comment model
    new_comment = Comment(
        post_id = post_id,
        text = comment.text,
        vva_user_id = user_id,
    )
    # Store in the DB
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)

    return