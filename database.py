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


last_msg = Table('last_msg', meta, autoload=True, autoload_with=engine, schema='bot')
people = Table('people', meta, autoload=True, autoload_with=engine, schema='bot')
groups = Table('groups', meta, autoload=True, autoload_with=engine, schema='bot')

def store_last_msg(groupId, msgId, msgText, name, senderId):
    conn = engine.connect()
    print("Select msg")
    s = select([last_msg]).where(last_msg.c.group_id == groupId)
    result = conn.execute(s)
    row = result.fetchall()
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
        print("Found message")
        return row
    result.close()
    conn.close()
    print("Done find message")

def add_person(userId, name):
    conn = engine.connect()
    print("Select person")
    s = select([people]).where(people.c.user_id == userId)
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

def add_group(groupId, botId):
    conn = engine.connect()
    print("Select group")
    s = select([groups]).where(groups.c.group_id == groupId)
    result = conn.execute(s)
    row = result.fetchall()
    if not row:
        print("Insert group")
        ins = groups.insert().values(group_id = groupId, bot_id = botId)
        result = conn.execute(ins)
    else:
        print("Update group")
        upd = groups.update().where(groups.c.group_id == groupId).values(bot_id = botId)
        result = conn.execute(upd)
    result.close()
    conn.close()
    print("Done group")

def find_dummy_bot(nname):
        conn = engine.connect()
        print("Select group")
        s = select([groups.c.bot_id]).where(groups.c.nickname == nname)
        result = conn.execute(s)
        row = result.fetchall()
        if not row:
            print("No dummy here")
            return None
        else:
            print("Found dummy")
            return row
        result.close()
        conn.close()
        print("Done find message")

def show_all_dummy():
        conn = engine.connect()
        print("Select group")
        s = select([groups.c.nickname])
        result = conn.execute(s)
        row = result.fetchall()
        if not row:
            print("No dummy bots")
            return None
        else:
            print("Got all dummies")
            return row
        result.close()
        conn.close()
        print("Done find dummies")

def get_user_id(user_name):
    conn = engine.connect()
    print("Select people")
    s = select([people.c.user_id]).where(people.c.current_name == user_name)
    result = conn.execute(s)
    row = result.fetchall()
    if not row:
        print("No person currently has that name")
        return None
    else:
        print("Found person")
        return row
    result.close()
    conn.close()
    print("Found "+ user_name + "'s id")
