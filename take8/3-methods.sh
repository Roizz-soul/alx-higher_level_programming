#!/bin/bash
# Scipt to take URL and display HTTP options
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
