#!/usr/bin/python3
"""
Script that takes in a URL
and displays the body of the response.
"""
import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(argv[1])
    status = response.status_code
    if status < 400:
        print(response.text)
    else:
        print("Error code: {}".format(status))
