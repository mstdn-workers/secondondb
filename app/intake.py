import os
import sys
import time
import threading
from db_treat import db_treat
from datetime import datetime, timedelta
from libs.mastodon.Mastodon import Mastodon
from libs.mastodon.streaming import StreamListener

client_name = os.getenv("CLIENT_NAME", "CLIENT")
api_base_url = os.getenv("API_BASE_URL", "---")
mastodon_user = os.getenv("MASTODON_USER", "---")
mastodon_pass = os.getenv("MASTODON_PASS", "---")
client_credfile_name = ".client.mstdncred"
user_credfile_name = ".user.mstdncred"

Mastodon.create_app(client_name, api_base_url = api_base_url, to_file = client_credfile_name)
mastodon = Mastodon(client_id=client_credfile_name, api_base_url = api_base_url)
mastodon.log_in(mastodon_user, mastodon_pass,to_file = user_credfile_name)

class MyStreamListener(StreamListener):
    def __init__(self):
        self.heartbeat_time = datetime.now()
        self.timeout_seconds = 60
        super(MyStreamListener, self).__init__()

    def heartbeat_check(self):
        while True:
            # inloop something
            compare_time = datetime.now() - self.heartbeat_time
            print("inloop: " + str(compare_time))
            if(compare_time > timedelta(seconds = self.timeout_seconds)):
                print("Emergency! connection lost!!")
            elif(compare_time > timedelta(seconds = self.timeout_seconds / 2 )):
                print("Warning! Heartbeat is delay!")
                self.docker_restart()
            time.sleep(10)

    def handle_stream(self, response):
        try:
            threading.Thread(target=self.heartbeat_check).start()
            super().handle_stream(response)
        except:
            # do something
            raise
    
    def handle_heartbeat(self):
        print(':thump')
        self.heartbeat_time = datetime.now()
        pass
    
    def on_update(self, status):
        print("update: "+str(status['id']))
        print(status.mentions)
        try:
            dsn = os.environ.get('DATABASE_URL')
            print(dsn)
            db = db_treat(dsn)
            db.insert(str(status['id']), status['json_str'])
        except:
            pass
        pass

    def on_delete(self, status_id):
        print("delete: "+str(status_id))
        pass

    def docker_restart(self):
        hostname = os.getenv("HOSTNAME", "get_stream")
        sys.exit()

if __name__ == "__main__":
    listener = MyStreamListener()
    mastodon.stream_local(listener)