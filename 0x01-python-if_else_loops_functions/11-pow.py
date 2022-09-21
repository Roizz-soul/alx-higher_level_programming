#!/usr/bin/python3
def pow(a, b):
    for i in range(b - 1):
        if b == 0:
            return 1
        else:
            a = a * a
        return a
