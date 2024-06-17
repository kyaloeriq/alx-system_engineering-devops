#!/usr/bin/python3
"""
Queries Reddit API, returns no. of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries Reddit API, returns no. of subscribers for a given subreddit.
    Parameters:
        subreddit (str): The name of the subreddit to query.
    Returns:
        str: "OK" for both valid and invalid subreddits.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': (
            'python:subreddit.subscriber.counter:v1.0 (by /u/yourusername)'
        )
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()

        if response.status_code == 200:
            data = response.json()
            if 'data' in data and 'subscribers' in data['data']:
                return data['data']['subscribers']
            else:
                return 0
        else:
            return 0
    except requests.exceptions.HTTPError:
        return 0
    except requests.exceptions.ConnectionError:
        return 0
    except requests.exceptions.Timeout:
        return 0
    except requests.exceptions.RequestException:
        return 0
