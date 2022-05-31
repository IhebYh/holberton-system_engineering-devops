#!/usr/bin/python3
"""
number_of_subscribers function
"""

import requests


def number_of_subscribers(subbreddit):
    """
    a function that queries REDDIT API and returns
    the number of subscribers
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
