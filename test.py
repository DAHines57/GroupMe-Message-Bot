import os
import giphypop
import random
import re
import subprocess
import requests
import traceback
import database
from database import store_last_msg
from database import find_last_msg
from libs import post_text
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask
from flask import request
from shade import shadeText
app = Flask(__name__)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


gif = giphypop.Giphy()
admin_sender_id = os.environ.get("ADMIN_SENDER_ID")

last_message = ''
@app.route('/callback/<bot_id>', methods=['POST'])
def parse_messages(bot_id):
    try:

        message = request.get_json()

        if message['sender_type'] != "user":
            return 'OK'

        """ Group Specific Actions """

        #Throw Shade
        if request.args.get('shade', '') != '':
            sender = message['name']
            if sender in shadeText:
                post_text(shadeText[sender], bot_id)

        """ Admin Actions """

        #Ventriloquism
        if request.args.get('dummy', '') != '' and message['sender_id'] == admin_sender_id:
            if message['text'].startswith("/dummy"):
                msg = message['text'][len("/dummy"):]
                post_text(msg, request.args.get('dummy', ''))


        """ Actions for all groups """

        # Say hello to anyone that says "Hi"
        if re.search(r"\bhi\b", message['text'].lower()):
            post_text("Hi " + message['name'].split(" ")[0] + "!", bot_id)

        # Post gif from Giphy
        if message['text'].startswith("/gif"):
            search = re.search(r"/gif (.*?)( \d+)?$", message['text'])
            (gif_search, num) = search.groups('1')
            if int(num) < 20:
                num = min(int(num), 5)
                for i in range(int(num)):
                    post_text(gif.translate(gif_search).media_url, bot_id)
            else:
                post_text("Can you not.", bot_id)

        # Clap a bunch
        if message['text'].startswith("/clap"):
            msg = message['text'][5:]
            msg = msg.upper()
            clap = '\U0001F44F'
            if message['sender_id'] == admin_sender_id:
                clap += '\U0001F3FF'
            msg = clap.join(msg.split())
            post_text(msg, bot_id)

        # Hurr Durr
        if message['text'].startswith("/durr"):
            msg_row = find_last_msg(message['group_id'])
            if msg_row:
                msg = msg_row[0]
                sender = msg_row[1].lower()
                lastSenderId = msg_row[2]
                low = (x.lower() for x in msg[0::2])
                upp = (x.upper() for x in msg[1::2])
                msg = ''.join(a + b for a, b in zip(low, upp))
                sender = re.sub(r"\s", "_", sender)
                durr_url = "https://memegen.link/custom/hurr_durr_i'm_" + sender + "/and_i_just_want_to_say.jpg?alt=http://i0.kym-cdn.com/entries/icons/original/000/022/940/spongebobicon.jpg"
                if lastSenderId != admin_sender_id or message['sender_id'] == admin_sender_id:
                    post_text(durr_url, bot_id)
                    post_text(msg, bot_id)
                else:
                    post_text("I'm sorry Dave, I'm afraid I can't do that.", bot_id)

        # Jokes
        if message['text'].startswith("/joke"):
            headers = {'Accept': 'text/plain'}
            joke = requests.get("https://icanhazdadjoke.com", headers=headers)
            joke.raise_for_status()
            post_text(joke.content.decode("UTF-8"), bot_id)

        """ Store Last Message """
        
        if message['sender_type'] == "user":
            store_last_msg(message['group_id'], message['id'], message['text'], message['name'], message['sender_id'])


        return 'OK'
    except:
            post_text(u'\U0001F916\u2620: ' + traceback.format_exc(), bot_id)
            return 'Not OK'
