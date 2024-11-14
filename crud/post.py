from typing import List
from uuid import UUID
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from schemas.post import PostBase
from models.post import Post

def get_all_posts(db: Session) -> List[Post]:
    return db.query(Post).all()

def get_post_by_id(db: Session, id: UUID) -> Post:
    post: Post = db.query(Post).filter(Post.id == id).first()
    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found"
        )
    return post

def add_post(db: Session, user_id: UUID, post: PostBase):
    db_post = Post(**post.model_dump(), vva_user_id=user_id)
    # Print the stuff in db_post
    # print(vars(db_post))
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return

def update_post_by_id(db: Session, post_id: UUID, updated_post: PostBase):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if db_post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found"
        )

    # Update fields
    db_post.title = updated_post.title
    db_post.text = updated_post.text
    db_post.featured = updated_post.featured

    db.commit()
    db.refresh(db_post)
    return