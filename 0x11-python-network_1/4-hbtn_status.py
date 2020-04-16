#!/usr/bin/python3
"""
fetches https://intranet.hbtn.io/status with package requests
"""

import requests

if __name__ == '__main__':
    resp = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(resp.content.decode('utf-8'))))
    print("\t- content: {}".format(resp.content.decode('utf-8')))
