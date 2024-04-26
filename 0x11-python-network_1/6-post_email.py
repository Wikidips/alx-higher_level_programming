#!/usr/bin/python3
"""
This script accepts a URL and an email address,
sends a POST request to the given URL with the email
as a parameter, and prints the response body.
"""
import requests
from sys import argv

if __name__ == "__main__":
    payload = {'email': argv[2]}
    response = requests.post(argv[1], data=payload)
    print(response.text)
