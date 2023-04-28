#!/bin/bash
# a script that takes in a URL, displays the size of the body of response
curl -s "$1" |wc -c
