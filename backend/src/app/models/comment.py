from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime
from sqlalchemy.sql import func

from app.db.base_class import Base


class Comment(Base):
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    post_id = Column(Integer, ForeignKey("post.id"))
    content = Column(Text, nullable=False)

    def __repr__(self):
        return f'<Comment "{self.content[:20]}...">'
