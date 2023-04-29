#!/usr/bin/python3
""" a Python script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable found in the header of
the response """
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    R = urllib.request.Request(url)
    with urllib.request.urlopen(R) as response:
        R_id = response.headers.get("X-Request-Id")
        print(R_id)
