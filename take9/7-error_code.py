#!/usr/bin/python3
"""A script to take in a URL, send a request and display a variable"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    resp = requests.get(url)
    if resp:
        print(resp.text)
    else:
        print("Error code: {}".format(resp.status_code))
