import requests
import time
import os
import json
from database import get_user_id, check_silenced

def post_text(user_text, bot_id):
    print("Posting message")
    time.sleep(1)
    if len(user_text.strip()) == 0:
        raise ValueError("Can't post empty message")
    if(not check_silenced(bot_id)[0]):
        requests.post('https://api.groupme.com/v3/bots/post', params = {'bot_id' : bot_id, 'text' : user_text}).raise_for_status()
    else:
        print("BOT IS SILENCED")

def post_text_mention(user_text, bot_id, mention_ids):
    print("Posting message with mention")
    time.sleep(1)
    if len(user_text.strip()) == 0:
        raise ValueError("Can't post empty message")
    if not isinstance(mention_ids, list):
        mention_ids = [mention_ids]
    print("User id: " + str(mention_ids))
    mentions = json.dumps(mention_ids)
    payload = {
      'text': user_text,
      'bot_id': bot_id,
      'attachments': [{ 'loci': [], 'type': "mentions", 'user_ids': [] }]
    };
    lociA = []
    for x in range(len(mention_ids)):
        payload.attachments[0]['loci'].append([0,0])

    payload.attachments[0]['loci'].append(mention_ids)


    if(not check_silenced(bot_id)[0]):
        requests.post('https://api.groupme.com/v3/bots/post', json=payload).raise_for_status()
        requests.post('http://requestbin.fullcontact.com/1neu8ut1', json=payload).raise_for_status()
    else:
        print("BOT IS SILENCED")

def get_group_info(group_id):
    access_token = os.environ.get("GROUPME_ACCESS_TOKEN")
    info = requests.get('https://api.groupme.com/v3/groups/' + group_id + '?token=' + access_token).json()
    return info
