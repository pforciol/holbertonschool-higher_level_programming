#!/bin/bash
# Displays the body of the response of a curl POST request
curl -sX POST -d "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD" "$1"
