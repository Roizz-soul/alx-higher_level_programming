#!/usr/bin/python3

Import sys


def safe_function(fct, *args):
    try:
        ans = fct(*args)
        return ans
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return None
