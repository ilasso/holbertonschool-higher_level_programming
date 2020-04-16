#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays
the body of the response.if the HTTP status code is greater than
or equal to 400, print: Error code: followed by the value
of the HTTP status code
using requests package
"""

import requests
from sys import argv

if __name__ == '__main__':

    url = argv[1]
    resp = requests.get(url)
    if resp.status_code == 200:
        print(resp.content.decode('utf-8'))
    else:
        print("Error code: {}".format(resp.status_code))
