#!/bin/bash
# Bash script that displays all HTTP methods
curl -sIX OPTIONS "$1" | awk -F': ' '/Allow/ { print $2 }'
