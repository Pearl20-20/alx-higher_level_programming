#!/usr/bin/python3
""" A script tha displays the body of a response after
    sending a POST request with email
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    mail = sys.argv[2]
    values = {'email': mail}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        print(html)
