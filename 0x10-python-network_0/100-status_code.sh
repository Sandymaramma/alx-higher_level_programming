#!/bin/bash
# Bash script that sends GET request and display status code of response
curl -so /dev/null -w '%{http_code}' "$1"
