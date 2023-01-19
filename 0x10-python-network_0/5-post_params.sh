#!/bin/bash
# script to send post request, parameters and display bdy of response
curl -sX POST -d 'email=test@gmail.com&subject=I will always be here for PLD' "$1"
