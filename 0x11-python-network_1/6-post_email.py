#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of
the response (decoded in utf-8)
using requests package
"""

import requests
from sys import argv

if __name__ == '__main__':

    url = argv[1]
    email = argv[2]
    dictdatain = {'email': email}
    req = requests.post(url, data=dictdatain)
    print(req.content.decode('utf-8'))
