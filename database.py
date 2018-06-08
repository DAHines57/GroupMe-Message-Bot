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


last_msg = Table('last_msg', meta, autoload=True, autoload_with=engine, schema='bot')
people = Table('people', meta, autoload=True, autoload_with=engine, schema='bot')
groups = Table('groups', meta, autoload=True, autoload_with=engine, schema='bot')

def store_last_msg(groupId, msgId, msgText, name, senderId):
    conn = engine.connect()
    print("Select msg")
    s = select([last_msg]).where(last_msg.c.group_id == groupId)
    print(groupId)
    result = conn.execute(s)
    row = result.fetchall()
    print(row)
    if not row:
        print("Insert msg")
        ins = last_msg.insert().values(group_id = groupId, msg_id = msgId, msg_txt = msgText,\
                                        sender_name = name, sender_id = senderId)
        result = conn.execute(ins)
    else:
        print("Update msg")
        upd = last_msg.update().where(last_msg.c.group_id == groupId).\
        values(group_id = groupId, msg_id = msgId, msg_txt = msgText, sender_name = name, sender_id = senderId)
        result = conn.execute(upd)
    result.close()
    conn.close()
    print("Done msg")

def find_last_msg(groupId):
    conn = engine.connect()
    s = select([last_msg.c.msg_txt, last_msg.c.sender_name, last_msg.c.sender_id]).where(last_msg.c.group_id == groupId)
    result = conn.execute(s)
    row = result.fetchone()
    if not row:
        print("No group by that name")
        return None
    else:
        print("Found")
        return row
    result.close()
    conn.close()
    print("Done find")

def add_person(userId, name):
    conn = engine.connect()
    print("Select person")
    s = select([people]).where(and_(people.c.user_id == userId))
    result = conn.execute(s)
    row = result.fetchall()
    if not row:
        print("Insert person")
        ins = people.insert().values(user_id = userId, current_name = name)
        result = conn.execute(ins)
    else:
        print("Update person")
        upd = people.update().where(people.c.user_id == userId).values(user_id = userId, current_name = name)
        result = conn.execute(upd)
    result.close()
    conn.close()
    print("Done person")

def add_group(groupId):
    conn = engine.connect()
    print("Select group")
    s = select([groups]).where(and_(groups.c.group_id == groupId))
    result = conn.execute(s)
    row = result.fetchall()
    if not row:
        print("Insert group")
        ins = groups.insert().values(group_id = groupId)
        result = conn.execute(ins)
