import uuid
from pydantic import (
    BaseModel,
)

from .models import Playlist

class PlaylistCreateSchema(BaseModel):
    title: str # user generated
    user_id: uuid.UUID # request.session user_id


        