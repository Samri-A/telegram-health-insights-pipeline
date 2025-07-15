from pydantic import BaseModel
from typing import List

class ProductReport(BaseModel):
    product_name: str
    mention_count: int

class ChannelActivity(BaseModel):
    date: str
    message_count: int

class MessageSearchResult(BaseModel):
    message_id: int
    message_text: str
    channel_name: str
