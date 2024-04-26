#!/usr/bin/python3
"""
Script that accepts a letter and sends a POST request to ...
with the letter as a parameter.
"""
import requests
from sys import argv

if __name__ == '__main__':
    q = argv[1] if len(argv) == 2 else ""
    url = 'http://0.0.0.0:5000/search_user'
    response = requests.post(url, data={'q': q})
    try:
        response_dict = response.json()
        id, name = response_dict.get('id'), response_dict.get('name')
        if not response_dict or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(id, name))
    except ValueError:
        print("Not a valid JSON")
