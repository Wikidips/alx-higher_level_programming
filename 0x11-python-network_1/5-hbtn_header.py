#!/usr/bin/python3
"""
This Python script accepts a URL, sends a request to that URL, and displays
the value of the 'X-Request-Id' variable found in the response header.
"""
import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(argv[1])
    print(response.headers.get('X-Request-Id'))
