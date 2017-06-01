import sys
import random
from libs import post_text

sadness_texts = [line.strip() for line in open('list of saddness.txt')]

post_text(random.choice(sadness_texts), sys.argv[1])
