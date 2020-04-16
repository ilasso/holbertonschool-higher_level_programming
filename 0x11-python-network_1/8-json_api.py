#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
from sys import argv

if __name__ == '__main__':
    if len(argv) > 1:
        letter = argv[1]
        dictdatain = {'q': letter}
    elif len(argv) == 1:
        dictdatain = {'q': ""}
    req = requests.post('http://0.0.0.0:5000/search_userxx', data=dictdatain)
    try:
        json = req.json()
    except ValueError:
        print("Not a valid JSON")
        exit()
    if json.__class__.__name__ == 'dict':
        if json == {}:
            print("No result")
        else:
            print("[{}] {}".format(json['id'], json['name']))
