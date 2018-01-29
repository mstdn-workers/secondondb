import h1don
import os
from mastodon import Mastodon, StreamListener


client_name = os.getenv("CLIENT_NAME", "CLIENT")
access_token = os.getenv("ACCESS_TOKEN", "")
api_base_url = os.getenv("API_BASE_URL", "")
mastodon_user = os.getenv("MASTODON_USER", "")
mastodon_pass = os.getenv("MASTODON_PASS", "")
client_credfile_name = "clientcred.txt"
user_credfile_name = "usercred.txt"

Mastodon.create_app(client_name, api_base_url = api_base_url, to_file = client_credfile_name)
mastodon = Mastodon(client_id=client_credfile_name, api_base_url = api_base_url)
mastodon.log_in(mastodon_user, mastodon_pass,to_file = user_credfile_name)

class MyStreamListener(StreamListener):
    def __init__(self):
        super(MyStreamListener, self).__init__()
        # self.logger = logging.getLogger(self.__class__.__name__)
    
    def handle_stream(self, response):
        try:
            super().handle_stream(response)
        except:
            # do something
            raise
    
    def on_update(self, status):
        # self.logger.info(status_info_string(status))
        print("update: "+status)
        pass

    def on_delete(self, status_id):
        # self.logger.info(f"status delete_event: {status_id}")
        print("delete: "+status_id)
        pass

if __name__ == "__main__":
    listener = QueueStreamListener(status_queue)
    mastodon.stream_local(listener)