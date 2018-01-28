import os
import requests
import json

class h1don:
    def __init__(self):
        self.mastodon_host = os.getenv("MASTODON_HOST", "")
        self.client_name = os.getenv("CLIENT_NAME", "CLIENT")
        self.redirect_uris = os.getenv("REDIRECT_URIS", "urn:ietf:wg:oauth:2.0:oob")
        self.scopes = os.getenv("SCOPES", "read write follow")
        self.client_id = os.getenv("CLIENT_ID", "")
        self.client_secret = os.getenv("CLIENT_SECRET", "")
        self.access_token = os.getenv("ACCESS_TOKEN", "")

    def get_LTL_stream(self):
        event = ""
        headers = {
            'Authorization': "Bearer "+self.access_token,
        }
        res = requests.get('https://'+self.mastodon_host+'/api/v1/streaming/public/local', headers=headers, stream=True)
        for line in res.iter_lines():
            line_str = line.decode('utf-8')
            if "event: update" in line_str:
                event = "update"
            if "event: delete" in line_str:
                event = "delete"
            if "data: " in line_str:
                line_str = line_str.lstrip('data: ')
                print(event + ': ' + line_str)