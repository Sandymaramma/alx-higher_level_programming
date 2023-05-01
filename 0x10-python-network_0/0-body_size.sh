#!/bin/bash
# Bash script that displays size of body of response
curl -so /dev/null -w '%{size_download}\n' "$1"
