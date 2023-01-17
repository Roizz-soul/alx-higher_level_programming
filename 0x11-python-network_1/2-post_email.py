#!/usr/bin/python3
"""A script to take in a URL, send a request and display a variable"""

import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email" = sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    with urllib.request.urlopen(url)\
      as response:
        result = response.read
    print(result)
