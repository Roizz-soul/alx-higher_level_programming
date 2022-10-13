#!/usr/bin/python3


Import sys


def safe_function(fct, *args):
    try:
        ans = fct(*args)
        return ans
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return None
