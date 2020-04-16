#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the body of
the response (decoded in utf-8). manage urllib.error.HTTPError exceptions
and print: Error code: followed by the HTTP status code
"""

import urllib.request
import urllib.parse
from sys import argv

if __name__ == '__main__':

    url = argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            resp = response.read()
            print(resp.decode('utf-8'))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
