from pydantic import BaseModel


class Message(BaseModel):
    date: str
    image_base64: str
    camera_id: int
