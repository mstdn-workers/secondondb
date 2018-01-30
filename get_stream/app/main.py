import os
from mastodon import Mastodon, StreamListener

client_name = os.getenv("CLIENT_NAME", "CLIENT")
api_base_url = os.getenv("API_BASE_URL", "---")
mastodon_user = os.getenv("MASTODON_USER", "---")
mastodon_pass = os.getenv("MASTODON_PASS", "---")
client_credfile_name = "client.mstdncred"
user_credfile_name = "user.mstdncred"

Mastodon.create_app(client_name, api_base_url = api_base_url, to_file = client_credfile_name)
mastodon = Mastodon(client_id=client_credfile_name, api_base_url = api_base_url)
mastodon.log_in(mastodon_user, mastodon_pass,to_file = user_credfile_name)


# dict_keys(['id', 'created_at', 'in_reply_to_id', 'in_reply_to_account_id', 'sensitive', 'spoiler_text', 'visibility', 'language', 'uri', 'content', 'url', 'reblogs_count', 'favourites_count', 'reblog', 'application', 'account', 'media_attachments', 'mentions', 'tags', 'emojis'])

class MyStreamListener(StreamListener):
    def __init__(self):
        super(MyStreamListener, self).__init__()

    def handle_stream(self, response):
        try:
            super().handle_stream(response)
        except:
            # do something
            raise
    
    def on_update(self, status):
        print("update: "+str(status['id']))
        pass

    def on_delete(self, status_id):
        print("delete: "+str(status_id))
        pass

if __name__ == "__main__":
    listener = MyStreamListener()
    mastodon.stream_local(listener)