#!/usr/bin/python3
"""A script to take in a URL, send a request and display a variable"""

import urllib.request
import urllib.parse
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            result = response.read()
            print(result.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
