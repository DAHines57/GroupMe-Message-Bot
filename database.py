import os
import psycopg2
import sqlalchemy
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from os.path import join, dirname

database_url = os.environ.get("DATABASE_URL")
engine = create_engine(database_url)

Base = declarative_base(engine)
meta=MetaData(bind=engine)
conn = engine.connect()

last_msg = Table('last_msg', meta, autoload=True, autoload_with=engine, schema='bot')

def store_last_msg(groupId, msgId, msgText, name, senderID):
     s=select([last_msg]).where(last_msg.c.group_id == groupId)
     result = conn.execute(s)
     row = result.fetchall()
     result.close()
     if not row:
         ins = last_msg.insert().values(group_id = groupId, msg_id = msgId, msg_text = msgText, sender_name = name, sender_id = senderID)
         result = conn.execute(ins)
     else:
         upd = last_msg.update().where(last_msg.c.group_id == groupId).\
         values(group_id = groupId, msg_id = msgId, msg_text = msgText, sender_name = name, sender_id = senderID)
         result = conn.execute(upd)
