from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

class LTL_Bucket(Base):
    __tablename__ = 'localtimeline'
    id = Column(String(32), primary_key=True)
    json_str = Column(Text(), nullable=False)
    uri = Column(String(256), nullable=False)
    url = Column(String(256), nullable=False)
    account_id = Column(String(32), ForeignKey('account.id'))
    account = relationship(account_Bucket)
    in_reply_to_id = Column(String(32), nullable=True)
    in_reply_to_account_id = Column(String(32), nullable=True)
    # reblog
    content = Column(Test, nullable=False)
    created_at = Column(Datetime(timezone=True), nullable=False)
    emojis = Column(postgresql.ARRAY(str))
    reblogs_count = Column(Integer, nullable=False)
    favourites_count = Column(Integer, nullable=False)
    # reblogged
    # favourited
    # muted
    sensitive = Column(Boolean, nullable=False)
    spoiler_text = Column(Test, nullable=False)
    visibility = Column(String(32), nullable=False)
    media_attachments = relationship('media_attachments_Bucket', backref='localtimeline')
    mentions = relationship('mention_Bucket', backref='localtimeline')
    tags = relationship('tags_Bucket', backref='localtimeline')
    application = relationship('application_Bucket', backref='localtimeline')
    language = Column(String(32), nullable=False)
    # pinned

class account_Bucket(Base):
    __tablename__ = 'account'
    id = Column(String(32), primary_key=True)
    username = Column(String(32), nullable=False)
    acct = Column(String(32), nullable=False)
    display_name = Column(String(32), nullable=False)
    locked = Column(Boolean, nullable=False)
    created_at = Column(Datetime(timezone=True), nullable=False)
    followers_count = Column(Integer, nullable=False)
    following_count = Column(Integer, nullable=False)
    statuses_count = Column(Integer, nullable=False)
    note = Column(Text(), nullable=False)
    url = Column(String(32), nullable=False)
    avatar = Column(String(32), nullable=False)
    avatar_static = Column(String(32), nullable=False)
    header = Column(String(32), nullable=False)
    header_static = Column(String(32), nullable=False)
    moved = Column(String(32), nullable=True)

class media_attachments_Bucket(Base):
    __tablename__ = 'media_attachments'
    id = Column(String(32), primary_key=True)
    media_type = Column(String(16), nullable=False) 
    url = Column(String(256), nullable=False)
    remote_url = Column(String(256), nullable=False)
    preview_url = Column(String(256), nullable=False)
    text_url = Column(String(256), nullable=False)
    meta = Column(String(256), nullable=False)
    description = Column(String(256), nullable=False)
    status_id = Column(String(32), nullable=False, ForeignKey('localtimeline.id'))

class mentions_Bucket(Base):
    __tablename__ = 'mentions'
    url = Column(String(32), nullable=False)
    username = Column(String(32), nullable=False)
    acct = Column(String(32), nullable=False)
    id = Column(String(32), primary_key=True)
    status_id = Column(String(32), nullable=False, ForeignKey('localtimeline.id'))

class tags_Bucket(Base):
    name = Column(String(256), nullable=False)
    url = Column(String(256), nullable=False)
    status_id = Column(String(32), nullable=False, ForeignKey('localtimeline.id'))
 
 class application_Bucket(Base):
    name = Column(String(256), nullable=False)
    website = Column(String(256), nullable=True)
    status_id = Column(String(32), nullable=True, ForeignKey('localtimeline.id'))     
