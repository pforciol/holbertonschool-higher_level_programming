#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status."""

from urllib import request

if __name__ == "__main__":
    with request.urlopen("https://intranet.hbtn.io/status") as page:
        content = page.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
