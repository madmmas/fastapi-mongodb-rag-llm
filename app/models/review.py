from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Review(BaseModel):
    _id: str
    date: Optional[datetime] = None
    listing_id: str
    reviewer_id: str
    reviewer_name: Optional[str] = None
    comments: Optional[str] = None
