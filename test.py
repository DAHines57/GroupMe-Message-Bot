import os
import giphypop
import random
import re
import subprocess
import requests
import traceback
from libs import post_text
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask
from flask import request
from shade import shadeText
app = Flask(__name__)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

responses = {'jlaw': 'JOHNNY LAW', 'jar': 'CONSEQUENCE JAR'}
gif = giphypop.Giphy()

last_message = ''
@app.route('/callback/<bot_id>', methods=['POST'])
def parse_messages(bot_id):
    try:
        global last_message
        message = request.get_json()

        if message['sender_type'] != "user":
            return 'OK'

        """ Group Specific Actions """

        # BUPD Things
        if request.args.get('bupd', '') != '':
            if re.search(r"\bbupd\b", message['text'].lower()):
                post_text(responses[request.args.get('bupd','')], bot_id)

        # CONSEQUENCE
        if request.args.get('dorm', '') != '':
            if re.search(r"\bdorm[Ss]?\b", message['text'].lower()):
                post_text(responses[request.args.get('dorm','')], bot_id)

        #Professionalism
        if request.args.get('punct', '') != '':
            if not (message['text'].strip().endswith((".","?","!"))):
                post_text("In the spirit of being professional, all messages must end with proper punctuation.", bot_id)

        #Throw Shade
        if request.args.get('shade', '') != '':
            sender = message['name']
            if sender in shadeText:
                post_text(shadeText[sender], bot_id)

        """ Admin Actions """

        #Ventriloquism
        if request.args.get('dummy', '') != '' and message['name'] == "Dylan Hines":
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
            if message['sender_id'] == '19791433':
                clap += '\U0001F3FF'
            msg = clap.join(msg.split())
            post_text(msg, bot_id)

        # Hurr Durr
        if message['text'].startswith("/durr"):
            msg = last_message['text'] + ' '
            low = (x.lower() for x in msg[0::2])
            upp = (x.upper() for x in msg[1::2])
            msg = ''.join(a + b for a, b in zip(low, upp))
            sender = message['name'].lower()
            sender = re.sub(r"\s", "_", sender)
            durr_url = "https://memegen.link/custom/hurr_durr_i'm_" + sender + "/and_i_just_want_to_say.jpg?alt=http://i0.kym-cdn.com/entries/icons/original/000/022/940/spongebobicon.jpg"
            post_text(durr_url, bot_id)
            post_text(msg, bot_id)


        # Jokes
        if message['text'].startswith("/joke"):
            headers = {'Accept': 'text/plain'}
            joke = requests.get("https://icanhazdadjoke.com", headers=headers)
            joke.raise_for_status()
            post_text(joke.content.decode("UTF-8"), bot_id)

        last_message = message

        return 'OK'
    except:
            post_text(u'\U0001F916\u2620: ' + traceback.format_exc(), bot_id)
            return 'Not OK'
