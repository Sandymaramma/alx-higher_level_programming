#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL and displays the value """

if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys

    try:
        with urllib.request.urlopen(sys.argv[1]) as r:
            print(r.getheader('X-Request-Id'))
    except (urllib.error.URLError, IndexError) as e:
        print(e)
