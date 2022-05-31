#!/usr/bin/python3
"""
recurse function
"""

import requests


def recurse(subbreddit, hot_list=[], after=None):
    """
    a function that queries REDDIT API and returns
    all the posts in a subbredit
    """
    if subbreddit is None or type(subbreddit) is not str:
        print(None)
    req = requests.get("https://www.reddit.com/r/{}/hot.json"
                       .format(subbreddit),
                       headers={'User-Agent': 'RedditAPI(by IhebYh)'},
                       params={'after': after}).json()
    after = req.get("data", {}).get("after", None)
    posts = req.get("data", {}).get("children", None)
    if posts is None or (len(posts) > 0 and posts[0].get('kind') != 't3'):
        if len(hot_list) == 0:
            return (None)
        return hot_list
    else:
        for post in posts:
            hot_list.append(post.get('data', {}).get('title', None))
    if after is None:
        if len(hot_list) == 0:
            return None
        return hot_list
    else:
        return recurse(subbreddit, hot_list, after)
