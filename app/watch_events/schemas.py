import uuid
from typing import Optional
from pydantic import BaseModel


class WatchEventSchema(BaseModel):
    host_id: str
    start_time: float
    end_time: float
    duration: float
    complete: bool
    path: Optional[str]
