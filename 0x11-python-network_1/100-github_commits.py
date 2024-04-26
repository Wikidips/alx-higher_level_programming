#!/usr/bin/python3
"""
Script that accepts two arguments to solve a challenge
"""
import requests
from sys import argv

if __name__ == '__main__':
    url = f"https://api.github.com/repos/{argv[1]}/{argv[2]}/commits"
    response = requests.get(url)
    commits = response.json()
    for commit in commits[:10]:
        print(f"{commit.get('sha')}: {commit.get('commit').get('author').get('name')}")
