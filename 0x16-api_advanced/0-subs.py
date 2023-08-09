#!/usr/bin/python3
"""
contains one function that returns the number of subscribers for a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    """
    headers = {
        'User-Agent': 'Windows:alx_scripts_python:v1.0.0 (/u/Alecky3)'
    }
    res = requests.get(
        'https://www.reddit.com/r/{}/about/.json'.format(subreddit),
        headers=headers,
        allow_redirects=False
    )
    if res.status_code == 200:
        return res.json()['data']['subscribers']
    return 0
