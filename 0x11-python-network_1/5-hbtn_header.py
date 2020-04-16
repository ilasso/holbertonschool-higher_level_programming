#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the value of
the X-Request-Id variable found in the header of the response.
only use requests package
"""

import requests
from sys import argv

if __name__ == '__main__':
    resp = requests.get(argv[1])
    if 'X-Request-Id' in resp.headers:
        print(resp.headers['X-Request-Id'])
