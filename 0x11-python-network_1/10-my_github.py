#!/usr/bin/python3
"""Python script that takes GitHub credentials (username and
password) and uses the GitHub API to display the user id."""

import requests
from sys import argv

if __name__ == "__main__":
    auth = (argv[1], argv[2])
    request = requests.get("https://api.github.com/user", auth=auth)
    print(request.json().get("id"))
