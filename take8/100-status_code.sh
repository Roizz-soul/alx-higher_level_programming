#!/bin/bash
# script that gets only th status code of url given
curl -s -o /dev/null -w "%{http_code}" "$1"
