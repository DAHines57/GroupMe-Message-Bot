import requests

def post_text(user_text, bot_id):
    requests.post('https://api.groupme.com/v3/bots/post', params = {'bot_id' : bot_id, 'text' : user_text})
