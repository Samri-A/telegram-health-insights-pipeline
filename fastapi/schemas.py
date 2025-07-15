from pydantic import BaseModel
from typing import Optional

class TopProduct(BaseModel):
    product_name: str
    mention_count: int

    class Config:
        orm_mode = True

class ChannelActivity(BaseModel):
    date: str
    message_count: int

    class Config:
        orm_mode = True

class SearchResult(BaseModel):
    message_id: int
    channel_name: str
    message_text: str
    date: str

    class Config:
        orm_mode = True
