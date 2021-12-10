from urllib.parse import parse_qs, urlparse


def extract_video_id(url):
    # Source: https://stackoverflow.com/a/54383711
    # Examples:
    # - http://youtu.be/nNpvWBuTfrc
    # - http://www.youtube.com/watch?v=nNpvWBuTfrc&feature=feedu
    # - http://www.youtube.com/embed/nNpvWBuTfrc
    # - http://www.youtube.com/v/nNpvWBuTfrc?version=3&amp;hl=en_US
    query = urlparse(url)
    if query.hostname == "youtu.be":
        return query.path[1:]
    if query.hostname in {"www.youtube.com", "youtube.com"}:
        if query.path == "/watch":
            return parse_qs(query.query)["v"][0]
        if query.path[:7] == "/watch/":
            return query.path.split("/")[1]
        if query.path[:7] == "/embed/":
            return query.path.split("/")[2]
        if query.path[:3] == "/v/":
            return query.path.split("/")[2]
        # # below is optional for playlists
        # if query.path[:9] == "/playlist":
        #     return parse_qs(query.query)["list"][0]
    return None