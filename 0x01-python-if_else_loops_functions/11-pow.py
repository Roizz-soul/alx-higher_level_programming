#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    elif b > 0:
        for i in range(abs(b) - 1):
            a = a * a
    else:
        a = 1 / a
        for i in range(abs(b) - 1):
            a = a * (1 / a)
    return a
