#!/bin/bash
# sends a json post request to url
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
