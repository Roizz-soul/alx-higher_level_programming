#!/usr/bin/python3
"""A script to take in a URL, send a request and display a variable"""

import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1])\
      as response:
        result = dict(response.headers)
    print(result.get('X-Request-Id'))
