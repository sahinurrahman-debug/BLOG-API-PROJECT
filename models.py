from sqlalchemy import String, Integer, Column,Text
from database import Base

#blog table
class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(Text)