import sys
import icalendar
import requests
import pytz
from datetime import datetime, timedelta
from libs import post_text
from icalendar import Calendar

r = requests.get(sys.argv[2])
icsData = r.text

cal = Calendar.from_ical(icsData)

for evt in cal.subcomponents:
    start = evt.decoded('DTSTART')
    now = datetime.now(tz=pytz.utc)
    time_left = start - now
    if timedelta(minutes=0) < time_left < timedelta(minutes=10):
        post_text(evt.decoded('SUMMARY'), sys.argv[1])
