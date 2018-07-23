import urbandict as ud

# Urban dictionary define something
def urban_define(text):
    defs = ud.define(text)[0:len(text)]
    word = defs[0]['word']
    return word[0:len(text)] + ": " + defs[0]['def']
