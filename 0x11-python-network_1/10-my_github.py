#!/usr/bin/python3
"""takes your Github credentials (username and password) and uses the Github API
to display your id"""
from sys import argv
from requests import get, auth


if __name__ == "__main__":
    auth = auth.HTTPBasicAuth(argv[1], argv[2])
    result = get("https://api.github.com/user", auth=auth)
    print(result.json().get("id"))
