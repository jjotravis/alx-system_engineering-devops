#!/usr/bin/python3
"""Queries the reddit API
Returns number of subscribers for a subreddit
if subreddit is invalid return 0"""

import requests


def number_of_subscribers(subreddit):
    """Function to query subreddit and
    return number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}

    # try:
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subs = data.get('data').get('subscribers')
        return subs
    else:
        return 1
    # except Exception as e:
        # return 0
