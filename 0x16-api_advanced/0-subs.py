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
        return 0
    req = requests.get("https://www.reddit.com/r/{}/about.json"
                       .format(subbreddit))
    subs_number = req.get("data", {}).get("subscribers", 0)
    return subs_number
