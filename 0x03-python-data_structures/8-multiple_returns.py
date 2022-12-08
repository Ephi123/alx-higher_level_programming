#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    fir_char = sentence[0] if length > 0 else "None"
    tup = length, fir_char
    return(tup)
