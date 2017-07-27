import os
import giphypop
import random
import re
import subprocess
from libs import post_text
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask
from flask import request
app = Flask(__name__)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

responses = {'jlaw': 'JOHNNY LAW', 'jar': 'CONSEQUENCE JAR'}
gif = giphypop.Giphy()


@app.route('/callback/<bot_id>', methods=['POST'])
def parse_messages(bot_id):
    try:
        message = request.get_json()
        if message['sender_type'] != "user":
            return 'OK'

        """ Group Specific Actions"""

        # BUPD Things
        if request.args.get('bupd', '') != '':
            if re.search(r"\bbupd\b", message['text'].lower()):
                post_text(responses[request.args.get('bupd','')], bot_id)

        # CONSEQUENCE
        if request.args.get('dorm', '') != '':
            if re.search(r"\bdorm[Ss]?\b", message['text'].lower()):
                post_text(responses[request.args.get('dorm','')], bot_id)


        """ Actions for all groups"""

        # Say hello to anyone that says "Hi"
        if re.search(r"\bhi\b", message['text'].lower()):
            post_text("Hi " + message['name'].split(" ")[0] + "!", bot_id)

        # Post gif from Giphy
        if message['text'].startswith("/gif"):
            gif_search = message['text'][5:]
            post_text(gif.translate(gif_search).media_url, bot_id)

        return 'OK'
    except Exception as e:
            post_text(u'\U0001F916\u2620: ' + str(e), bot_id)
            return 'Not OK'
