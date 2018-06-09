import requests
import time
from database import get_user_id

def post_text(user_text, bot_id):
    time.sleep(1)
    if len(user_text.strip()) == 0:
        raise ValueError("Can't post empty message")
    requests.post('https://api.groupme.com/v3/bots/post', params = {'bot_id' : bot_id, 'text' : user_text}).raise_for_status()

def post_text_mention(user_text, bot_id, user_name):
    time.sleep(1)
    if len(user_text.strip()) == 0:
        raise ValueError("Can't post empty message")
    mention_id = get_user_id(user_name)[0]
    print("User id: " + mention_id)
    requests.post('https://api.groupme.com/v3/bots/post', params = {'attachments' :[{"loci":[[0,12]],"type":"mentions","user_ids":[mention_id]}]
    ,'bot_id' : bot_id, 'text' : user_text}).raise_for_status()



yo@Dylan Hines
