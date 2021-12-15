import uuid # timeuuid

from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

from app import config

settings = config.get_settings()


class WatchEvent(Model):
    __keyspace__ = settings.keyspace
    host_id = columns.Text(primary_key=True)
    event_id = columns.TimeUUID(primary_key=True, clustering_order="DESC", default=uuid.uuid1)
    user_id = columns.UUID(primary_key=True)
    path = columns.Text()
    start_time = columns.Double()
    end_time = columns.Double()
    duration = columns.Double()
    complete = columns.Boolean(default=False)


    @property
    def completed(self):
        return (self.duration * 0.97) < self.end_time

    @staticmethod
    def get_resume_time(host_id, user_id):
        resume_time = 0
        obj = WatchEvent.objects.allow_filtering().filter(host_id=host_id, user_id=user_id).first()
        if obj is not None:
            if not obj.complete or not obj.completed:
                resume_time = obj.end_time
        return resume_time
