import os
import requests
import werkzeug
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask
from flask import request
app = Flask(__name__)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

bupd_responses = {'fuzz': "Oh shit, it's the fuzz!", 'jlaw': 'Johnny Law!'}

def post_text(user_text, bot_id):
    requests.post('https://api.groupme.com/v3/bots/post', params = {'bot_id' : bot_id, 'text' : user_text})

@app.route('/callback/<bot_id>', methods=['POST'])
def parse_messages(bot_id):
    message = request.get_json()
    if message['sender_type'] != "user":
        return 'OK'

    # BUPD Things
    if request.args.get('bupd', 'off') != 'off':
        if "bupd" in message['text'].lower():
            post_text(bupd_responses[request.args.get('bupd','')], bot_id)

    # Say hello to anyone that says "Hi"
    if "Hi" in message['text']:
        x=5/0
        post_text("Hi " + message['name'].split(" ")[0] + "!", bot_id)

    """
    # Get annoyed at long texts
    if len(message['text']) >= 300:
        post_text("Cool story bro.")
    """
    return 'OK'

@app.errorhandler(werkzeug.exceptions.InternalServerError)
def handle_error(e):
    post_text(u'\U0001F916\U0001F915: ' + str(e), bot_id)
    return 'Not OK'
