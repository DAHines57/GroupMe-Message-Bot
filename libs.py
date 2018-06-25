import requests
import time
import os
import json
from database import get_user_id, check_silenced

# Post a normal message to a group with text
def post_text(user_text, bot_id):
    print("Posting message")
    time.sleep(1)
    if len(user_text.strip()) == 0:
        raise ValueError("Can't post empty message")
    if(not check_silenced(bot_id)[0]):
        requests.post('https://api.groupme.com/v3/bots/post', params = {'bot_id' : bot_id, 'text' : user_text}).raise_for_status()
    else:
        print("BOT IS SILENCED")

# Post a normal message but also mention someone
def post_text_mention(user_text, bot_id, mention_ids):
    print("Posting message with mention")
    time.sleep(1)
    if len(user_text.strip()) == 0:
        raise ValueError("Can't post empty message")
    if not isinstance(mention_ids, list):
        mention_ids = [mention_ids]
    print("User id: " + str(mention_ids))
    payload = {
      'text': user_text,
      'bot_id': bot_id,
      'attachments': [{ 'loci': [], 'type': "mentions", 'user_ids': []  }]
    };
    for x in range(len(mention_ids)):
        payload['attachments'][0]['loci'].append([0,0])

    payload['attachments'][0]['user_ids'] = mention_ids

    print(payload)

    if(not check_silenced(bot_id)[0]):
        requests.post('https://api.groupme.com/v3/bots/post', json=payload).raise_for_status()
    else:
        print("BOT IS SILENCED")

# Remove a user from a group
def remove_user(group_id, membership_id, bot_id):
    print("Removing a user")
    access_token = os.environ.get("GROUPME_ACCESS_TOKEN")
    if(not check_silenced(bot_id)[0]):
        requests.post('https://api.groupme.com/v3/bots/groups/' + group_id + '/members/' + membership_id + '/remove' + '?token=' + access_token).raise_for_status()
        print("User removed.")
    else:
        print("BOT IS SILENCED")

# Snag the group JSON data
def get_group_info(group_id):
    access_token = os.environ.get("GROUPME_ACCESS_TOKEN")
    info = requests.get('https://api.groupme.com/v3/groups/' + group_id + '?token=' + access_token).json()
    return info
