#!/usr/bin/python3
"""
contains one function that prints the titles of the first top ten
subreddits
"""
import requests


def top_ten(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    """
    headers = {
        'User-Agent': 'Windows:alx_scripts_python:v1.0.0 (/u/Alecky3)'
    }
    res = requests.get(
        'https://www.reddit.com/r/{}/.json?sort=topt&limit=10'.format(subreddit),
        headers=headers,
        allow_redirects=False
    )
    if res.status_code == 200:
        for p in res.json()["data"]["children"][0:10]:
            print(p['data']['title'])
    else:
        print(None)
