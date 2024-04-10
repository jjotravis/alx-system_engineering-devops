#!/usr/bin/python3
"""Queries the reddit API
Returns list of all hot articles in a subreddit
if subreddit is invalid print None"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Function to query subreddit and
    return title of 1st 10 hot spots"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    hot = response.json().get('data')
    after = hot.get('after')
    count += hot.get('dist')
    for i in hot.get('children'):
        hot_list.append(i.get('data').get('title'))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
