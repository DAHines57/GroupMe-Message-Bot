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

sadness_texts = [line.strip() for line in open('list of saddness.txt')]

requests.post('https://api.groupme.com/v3/bots/post', params = {'bot_id' : sys.argv[1], 'text' : random.choice(sadness_texts)})
