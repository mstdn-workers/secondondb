CREATE TABLE localtimeline (
  id TEXT PRIMARY KEY,
  created_at timestamp [3],
  in_reply_to_id TEXT,
  in_reply_to_account_id TEXT,
  sensitive BOOLEAN,
  spoiler_text TEXT,
  visibility TEXT,
  language TEXT,
  uri TEXT,
  content TEXT,
  url TEXT,
  reblogs_count INT,
  favourites_count INT,
  reblog TEXT,
  application TEXT,
  account JSON,
  media_attachments JSON[],
  mentions TEXT[],
  tags TEXT[],
  emojis TEXT[]
);

