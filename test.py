import os
import requests
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask
app = Flask(__name__)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

bot_id = os.environ.get("BOT_ID")

@app.route('/post/<uText>')
def show_user_profile(uText):
    r = requests.post('https://api.groupme.com/v3/bots/post', params = {'bot_id' : bot_id, 'text' : uText})
    return 'Post: %s' % uText
