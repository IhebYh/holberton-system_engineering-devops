#!/usr/bin/python3
"""
top_ten function
"""

import requests


def top_ten(subbreddit):
    """
    a function that queries REDDIT API and returns
    the top ten posts in a subbredit
    """
    if subbreddit is None or type(subbreddit) is not str:
        print(None)
    req = requests.get("https://www.reddit.com/r/{}/hot.json"
                       .format(subbreddit),
                       headers={'User-Agent': 'RedditAPI(by IhebYh)'},
                       params={'limit': 10}).json()
    hot = req.get("data", {}).get("children", None)
    if hot is None or (len(hot) > 0 and hot[0].get('kind') != 't3'):
        print(None)
    else:
        for post in hot:
            print(post.get('data', {}).get('title', None))
