from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func

from app.db.base_class import Base


class Post(Base):
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    content = Column(Text)
    # comments = relationship('Comment', backref='post')

    def __repr__(self):
        return f'<Post "{self.title}">'
