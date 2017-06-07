import sys
import random
from pytz import timezone
from datetime import datetime
import pytz
from libs import post_text

sadness_texts = [line.strip() for line in open('list of saddness.txt')]

central = timezone('US/Central')
now = datetime.now(tz=pytz.utc)
if (8 <= now.astimezone(central).hour <= 21):
    x = random.randint(0, 144)
    if(x == 1):
        post_text(random.choice(sadness_texts), sys.argv[1])
    else:
        print(x)
