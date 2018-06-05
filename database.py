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

Last_msg = Table('Last_msg', meta, autoload=True, autoload_with=engine, schema='bot')
