import uuid
from app.config import get_settings
from app.users.models import User
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

settings = get_settings()

from .extractors import extract_video_id

class Video(Model):
    __keyspace__ = settings.keyspace
    host_id = columns.Text(primary_key=True) # YouTube, Vimeo
    db_id = columns.UUID(primary_key=True, default=uuid.uuid1) # UUID1
    host_service = columns.Text(default='youtube')
    url = columns.Text() # secure
    user_id = columns.UUID()
    # user_display_name

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"Video(email={self.email}, user_id={self.user_id})"

    @staticmethod
    def add_video(url, user_id=None):
        # extract video_id from url
        # video_id = host_id
        # Service API - YouTube / Vimeo / etc
        host_id = extract_video_id(url)
        if host_id is None:
            raise Exception("Invalid YouTube Video URL")
        user_id = User.check_exists(user_id)
        if user_id is None:
            raise Exception("Invalid user_id")
        # user_obj = User.by_user_id(user_id)
        # user_obj.display_name
        q = Video.objects.filter(host_id=host_id, user_id=user_id)
        if q.count() != 0:
            raise Exception("Video already added")
        return Video.create(host_id=host_id, user_id=user_id, url=url)



# class PrivateVideo(Video):
# pass