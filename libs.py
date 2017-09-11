import requests

def post_text(user_text, bot_id):
    if len(user_text.strip()) == 0:
        raise ValueError("Can't post empty message")
    requests.post('https://api.groupme.com/v3/bots/post', params = {'bot_id' : bot_id, 'text' : user_text}).raise_for_status()
