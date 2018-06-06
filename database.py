import os
import psycopg2
import sqlalchemy
from libs import post_text
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from os.path import join, dirname

database_url = os.environ.get("DATABASE_URL")
engine = create_engine(database_url)

Base = declarative_base(engine)
meta=MetaData(bind=engine)
conn = engine.connect()

last_msg = Table('last_msg', meta, autoload=True, autoload_with=engine, schema='bot')

def store_last_msg(groupId, msgId, msgText, name, senderId):
    print("Select")
    s=select([last_msg]).where(last_msg.c.group_id == groupId)
    print(groupId)
    result = conn.execute(s)
    row = result.fetchall()
    print(row)
    if not row:
        print("Insert")
        ins = last_msg.insert().values(group_id = groupId, msg_id = msgId, msg_txt = msgText,\
                                        sender_name = name, sender_id = senderId)
        result = conn.execute(ins)
    else:
        print("Update")
        upd = last_msg.update().where(last_msg.c.group_id == groupId).\
        values(group_id = groupId, msg_id = msgId, msg_txt = msgText, sender_name = name, sender_id = senderId)
        result = conn.execute(upd)
    result.close()
    print("Done")

def find_last_msg(groupId):
    s=select([last_msg.c.msg_txt, last_msg.c.sender_name, last_msg.c.sender_id]).where(last_msg.c.group_id == groupId)
    result = conn.execute(s)
    row = result.fetchone()
    if not row:
        print("No group by that name")
        return False
    else:
        return row
    result.close()
    print("Done")
