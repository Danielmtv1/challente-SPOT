from sqlalchemy import Column, DateTime, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Message(Base):
    __tablename__ = "Messages"
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    image_base64 = Column(Text)
    camera_id = Column(Integer, nullable=False)
