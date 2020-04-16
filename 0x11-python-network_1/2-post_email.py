#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of
the response (decoded in utf-8) takes in a URL,
sends a request to the URL and displays the value of
the X-Request-Id variable found in the header of the response.
"""

import urllib.request
import urllib.parse
from sys import argv

if __name__ == '__main__':

    url = argv[1]
    email = argv[2]
    dictdatain = {'email': email}
    data = urllib.parse.urlencode(dictdatain)
    data = data.encode('ascii')

    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        resp = response.read()
        print(resp.decode('utf-8'))
