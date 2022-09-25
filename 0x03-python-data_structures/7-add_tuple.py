#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = list(tuple_a)
    b = list(tuple_b)
    c = []
    a.append(0)
    a.append(0)
    b.append(0)
    b.append(0)
    c.append(a[0] + b[0])
    c.append(a[1] + b[1])
    return tuple(c)
