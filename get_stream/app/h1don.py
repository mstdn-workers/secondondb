import os
import requests
import json
import time
import subprocess
from datetime import datetime

class h1don:
    def __init__(self):
        self.heartbeat = datetime.now()
        self.mastodon_host = os.getenv("MASTODON_HOST", "")
        self.client_name = os.getenv("CLIENT_NAME", "CLIENT")
        self.redirect_uris = os.getenv("REDIRECT_URIS", "urn:ietf:wg:oauth:2.0:oob")
        self.scopes = os.getenv("SCOPES", "read write follow")
        self.client_id = os.getenv("CLIENT_ID", "")
        self.client_secret = os.getenv("CLIENT_SECRET", "")
        self.access_token = os.getenv("ACCESS_TOKEN", "")

    def get_LTL_stream(self):
        event = ""
        s = requests.Session()
        s.headers.update({'Authorization': "Bearer "+self.access_token,})
        s.stream = True
        res = s.get('https://'+self.mastodon_host+'/api/v1/streaming/public/local')
        for line in res.iter_lines():
            line_str = line.decode('utf-8')
            if ":thump" in line_str:
                print(":thump " + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
                self.heartbeat = datetime.now()
            if "event: update" in line_str:
                event = "update"
            if "event: delete" in line_str:
                event = "delete"
            if "data: " in line_str:
                line_str = line_str.lstrip('data: ')
                print(event + ': ' + line_str)

    def heartbeat_check(self):
        delay = 15
        time.sleep(delay)
        if datetime.now() - self.heartbeat > delay:
            self.docker_restart()

    def docker_restart(self):
        hostname = os.getenv("HOSTNAME", "get_stream")
        subprocess.call("docker restart " + hostname)