#!/usr/bin/python3
"""Queries the reddit API
Returns top 10 hot spots
if subreddit is invalid print None"""

import requests


def top_ten(subreddit):
    """Function to query subreddit and
    return title of 1st 10 hot spots"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            children = data.get('data').get('children')
            for i in range(10):
                print(children[i].get('data').get('title'))
        else:
            print('None')
    except Exception as e:
        print("None")
