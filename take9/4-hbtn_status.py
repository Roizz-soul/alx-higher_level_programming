#!/usr/bin/python3
"""A script to fetch resources from an http site"""

import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    resp = requests.get(url, auth=('user', 'pass'))
    print("Body response:")
    print("\t- type: {}".format(type(resp.text)))
    print("\t- content: {}".format(resp.text))
