import os
import requests
import werkzeug
import giphypop
import random
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask
from flask import request
app = Flask(__name__)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

bupd_responses = {'jlaw': 'JOHNNY LAW'}
sadness_texts = [line.strip() for line in open('list of saddness.txt')]
gif = giphypop.Giphy()


def post_text(user_text, bot_id):
    requests.post('https://api.groupme.com/v3/bots/post', params = {'bot_id' : bot_id, 'text' : user_text})

@app.route('/callback/<bot_id>', methods=['POST'])
def parse_messages(bot_id):
    try:
        message = request.get_json()
        if message['sender_type'] != "user":
            return 'OK'

        # BUPD Things
        if request.args.get('bupd', 'off') != 'off':
            if "bupd" in message['text'].lower():
                post_text(bupd_responses[request.args.get('bupd','')], bot_id)

        # Say hello to anyone that says "Hi"
        if "Hi" in message['text']:
            post_text("Hi " + message['name'].split(" ")[0] + "!", bot_id)

        # Post gif from Giphy
        if message['text'].startswith("/gif"):
            gif_search = message['text'][5:]
            post_text(gif.translate(gif_search).media_url, bot_id)

        # Everything in life is suffering and sorrow
        if "sad" in message['text'].lower():
            post_text(random.choice(sadness_texts), bot_id)

        """
        # Get annoyed at long texts
        if len(message['text']) >= 300:
            post_text("Cool story bro.")
        """
        return 'OK'
    except Exception as e:
            post_text(u'\U0001F916\u2620: ' + str(e), bot_id)
            return 'Not OK'
