#!/usr/bin/python3
def multiple_returns(sentence):
    a = []
    a.append(len(sentence))
    if len(sentence) == 0:
        a.append("None")
    else:
        a.append(sentence[0])
    return tuple(a)
