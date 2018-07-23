import urbandict as ud

# Urban dictionary define something
def urban_define(text):
    defs = ud.define(text)
    return defs[0]['word'] + ": " + defs[0]['def']
