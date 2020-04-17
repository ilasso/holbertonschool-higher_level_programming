#!/usr/bin/python3
"""
takes your Github credentials (username and password) and uses
the Github API to display your id
"""

import requests
from sys import argv

if __name__ == '__main__':
    user = argv[1]
    passwd = argv[2]

    r = requests.get('https://api.github.com/user', auth=(user, passwd))
    if r.status_code == 200:
        json = r.json()
        print(json['id'])
    else:
        print("None")
