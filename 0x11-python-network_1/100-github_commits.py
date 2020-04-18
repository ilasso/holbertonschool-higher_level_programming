#!/usr/bin/python3
"""
prints github repository information
"""


if __name__ == '__main__':
    import sys
    import requests

    user = sys.argv[1]
    repo = sys.argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(user, repo)

    r = requests.get(url)
    for i in r.json()[0:10]:
        for j, k in i.items():
            if j == 'commit':
                sha = i['sha']
                name = k['author']['name']
                print("{}: {}".format(sha, name))
