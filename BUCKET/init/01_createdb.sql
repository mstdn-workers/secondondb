CREATE TABLE localtimeline (
  id TEXT PRIMARY KEY,
  json_str TEXT NOT NULL,
  account_id TEXT,
  in_reply_to_id TEXT,
  in_reply_to_account_id TEXT,
  reblog TEXT,
  content TEXT,
  created_at TIMESTAMP [3],
  sensitive TEXT,
  spoiler_text TEXT,
  visibility TEXT,
  media_attachments_id TEXT[],
  mentions_id TEXT[],
  tags_name TEXT[]
);

