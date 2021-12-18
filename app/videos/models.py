import uuid
from app.config import get_settings
from app.users.exceptions import InvalidUserIDException
from app.users.models import User
from app.shortcuts import templates

from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
from cassandra.cqlengine.query import (DoesNotExist, MultipleObjectsReturned)

settings = get_settings()

from .exceptions import (
    InvalidYouTubeVideoURLException, 
    VideoAlreadyAddedException
)
from .extractors import extract_video_id


# Unlisted Video -> video_id -> lock it down

class Video(Model):
    __keyspace__ = settings.keyspace
    host_id = columns.Text(primary_key=True) # YouTube, Vimeo
    db_id = columns.UUID(primary_key=True, default=uuid.uuid1) # UUID1
    host_service = columns.Text(default='youtube')
    title = columns.Text()
    url = columns.Text() # secure
    user_id = columns.UUID()


    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"Video(title={self.title}, host_id={self.host_id}, host_service={self.host_service})"

    def render(self):
        basename = self.host_service # youtube, vimeo
        template_name = f"videos/renderers/{basename}.html"
        context = {"host_id": self.host_id}
        t = templates.get_template(template_name)
        return t.render(context)

    def as_data(self):
        return {f"{self.host_service}_id": self.host_id, "path": self.path, "title": self.title}

    @property
    def path(self):
        return f"/videos/{self.host_id}"
    
    @staticmethod
    def get_or_create(url, user_id=None, **kwargs):
        host_id = extract_video_id(url)
        obj = None
        created = False
        try:
            obj = Video.objects.get(host_id=host_id)
        except MultipleObjectsReturned:
            q = Video.objects.allow_filtering().filter(host_id=host_id)
            obj = q.first()
        except DoesNotExist:
            obj = Video.add_video(url, user_id=user_id, **kwargs)
            created = True
        except:
            raise Exception("Invalid Request")
        return obj, created

    def update_video_url(self, url, save=True):
        host_id = extract_video_id(url)
        if not host_id:
            return None
        self.url = url
        self.host_id = host_id
        if save:
            self.save()
        return url

    @staticmethod
    def add_video(url, user_id=None, **kwargs):
        # extract video_id from url
        # video_id = host_id
        # Service API - YouTube / Vimeo / etc
        host_id = extract_video_id(url)
        if host_id is None:
            raise InvalidYouTubeVideoURLException("Invalid YouTube Video URL")
        user_exists = User.check_exists(user_id)
        if user_exists is None:
            raise InvalidUserIDException("Invalid user_id")
        # user_obj = User.by_user_id(user_id)
        # user_obj.display_name
        q = Video.objects.allow_filtering().filter(host_id=host_id) # , user_id=user_id)
        if q.count() != 0:
            raise VideoAlreadyAddedException("Video already added")
        return Video.create(host_id=host_id, user_id=user_id, url=url, **kwargs)



# class PrivateVideo(Video):
# pass