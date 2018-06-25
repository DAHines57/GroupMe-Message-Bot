import random
import os
import yaml

roast = yaml.load(open(os.path.dirname(__file__) + '/s_roast.yml'))

def generateInsult():
    column1 = random.choice(roast['column1'])
    column2 = random.choice(roast['column2'])
    column3 = random.choice(roast['column3'])
    txt = "\n" + "Thou", column1, column2, column3
    print(txt)
    return txt
