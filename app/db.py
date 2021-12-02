import pathlib
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.cqlengine import connection


BASE_DIR = pathlib.Path(__file__).resolve().parent

ASTRADB_CONNECT_BUNDLE = BASE_DIR / "unencrypted" / "astradb_connect.zip"

ASTRADB_CLIENT_ID= '<<CLIENT ID>>'
ASTRADB_CLIENT_SECRET= '<<CLIENT ID>>'

def get_session():
    cloud_config= {
            'secure_connect_bundle': ASTRADB_CONNECT_BUNDLE
    }
    auth_provider = PlainTextAuthProvider(ASTRADB_CLIENT_ID, ASTRADB_CLIENT_SECRET)
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    session = cluster.connect()
    connection.register_connection(str(session), session=session)
    connection.set_default_connection(str(session))
    return session