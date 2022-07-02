#!/usr/bin/python3
def multiple_returns(sentence):
    stuple = (len(sentence), sentence[0] if sentence else None)
    return(stuple)
