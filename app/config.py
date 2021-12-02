from functools import lru_cache
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    keyspace: str = Field(..., env='ASTRADB_KEYSPACE')
    db_client_id: str = Field(..., env='ASTRADB_CLIENT_ID')
    db_client_secret: str = Field(..., env='ASTRADB_CLIENT_SECRET')

    class Config:
        env_file = '.env'


@lru_cache
def get_settings():
    return Settings()