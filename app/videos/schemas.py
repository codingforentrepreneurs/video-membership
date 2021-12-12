from pydantic import (
    BaseModel,
    validator,
    root_validator
)

from app.users.exceptions import InvalidUserIDException


from .exceptions import (
    InvalidYouTubeVideoURLException, 
    VideoAlreadyAddedException
)
from .extractors import extract_video_id
from .models import Video

class VideoCreateSchema(BaseModel):
    url: str # user generated
    user_id: str # request.session user_id

    @validator("url")
    def validate_youtube_url(cls, v, values, **kwargs):
        url = v
        video_id = extract_video_id(url)
        if video_id is None:
            raise ValueError(f"{url} is not a valid YouTube URL")
        return url

    @root_validator
    def validate_data(cls, values):
        url = values.get("url")
        user_id = values.get("user_id")
        video_obj = None
        try:
            video_obj = Video.add_video(url, user_id=user_id)
        except InvalidYouTubeVideoURLException:
            raise ValueError(f"{url} is not a valid YouTube URL")
        except InvalidUserIDException:
            raise ValueError("There's a problem with your account, please try again.")
        except:
            raise ValueError("There's a problem with your account, please try again.")
        if video_obj is None:
            raise ValueError("There's a problem with your account, please try again.")
        if not isinstance(video_obj, Video):
            raise ValueError("There's a problem with your account, please try again.")
        return video_obj.as_data()


        