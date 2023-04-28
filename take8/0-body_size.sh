#!/bin/bash
# a script to take in a URL and display the size of the body of response
curl -s "$1" |wc -c
