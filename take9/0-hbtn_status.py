#!/usr/bin/python3
"""A script to fetch resources from an http site"""

import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status')\
      as response:
        result = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(result)))
    print("\t- content: {}".format(result))
    print("\t- utf8 content: {}".format(result.decode('utf-8')))
