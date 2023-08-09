#!/usr/bin/python3
import requests
"""
Defines number_of_subscribers function that returns the number of subscribes
for a subreddit
"""


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for the subreddit
    """
    if subreddit and isinstance(subreddit, str):
        url = f'https://www.reddit.com/r/{subreddit}/about.json'
        headers = {
            'User-Agent': 'Windows: alx_scripts_python:v1.0.0.0 (by u/Alecky3)'
            }
        req = requests.get(url, headers=headers, allow_redirects=False)
        if req.status_code == 200:
            return req.json().get("data").get("subscribers")
        else:
            return 0
    else:
        return 0
