from algoliasearch.search_client import SearchClient

from app import config


settings = config.get_settings()

def get_index():
    client = SearchClient.create(
            settings.algolia_app_id, 
            settings.algolia_api_key
    )
    index = client.init_index(settings.algolia_index_name)
    return index


def update_index():
    return 


def search_index(query):
    index = get_index()
    return index.search(query)