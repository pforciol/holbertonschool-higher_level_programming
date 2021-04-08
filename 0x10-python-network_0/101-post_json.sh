#!/bin/bash
# Displays the body of the response of a curl POST request with json
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
