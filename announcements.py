import sys
import icalendar
import requests
import pytz
from datetime import datetime, timedelta
from libs import post_text
from icalendar import Calendar
from database import find_bot_nname
import re

r = requests.get(sys.argv[2])
icsData = r.text

cal = Calendar.from_ical(icsData)

for evt in cal.subcomponents:
    print(evt.items())
    print(evt.subcomponents
    start = evt.decoded('DTSTART')
    now = datetime.now(tz=pytz.utc)
    time_left = start - now
    if timedelta(minutes=0) < time_left < timedelta(minutes=10):
        raw_text = str(evt.decoded('SUMMARY'))
        search = re.search(r"([^ ]+)\s(.+)", raw_text)
        (nname, message) = search.groups('1')
        nname = nname[2:]
        message = message[:-1]
        print(nname)
        print(message)
        bot_id = find_bot_nname(nname)
        if not bot_id:
            bot_id = sys.argv[1]
            post_text("I was supposed to post '" + message + "' to " + nname, bot_id)
        else:
            bot_id = bot_id[0][0]
            post_text(message, bot_id)
