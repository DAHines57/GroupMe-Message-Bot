import urbandictionary as ud

def urban_define(text):
    defs = ud.define(text)
    return defs[0].word + ": " + defs[0].definition
