from datetime import datetime # datetime.datetime
import uuid

from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

from app import config

settings = config.get_settings()

# [1, 2, 3] -> columns.Integer

class Playlist(Model):
    __keyspace__ = settings.keyspace
    db_id = columns.UUID(primary_key=True, default=uuid.uuid1)
    user_id = columns.UUID()
    updated = columns.DateTime(default=datetime.utcnow())
    host_ids = columns.List(value_type=columns.Text) # ["abc123"]
    title = columns.Text()
    