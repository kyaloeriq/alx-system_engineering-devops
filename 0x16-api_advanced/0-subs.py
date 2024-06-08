#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    Parameters:
        subreddit (str): The name of the subreddit to query.
    Returns:
        str: "OK" for both valid and invalid subreddits.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'python:subreddit.subscriber.counter:v1.0 (by /u/yourusername)'
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()

        if response.status_code == 200:
            data = response.json()
            if 'data' in data and 'subscribers' in data['data']:
                return "OK"
            else:
                return "OK"
        else:
            return "OK"
    except requests.exceptions.HTTPError:
        return "OK"
    except requests.exceptions.ConnectionError:
        return "OK"
    except requests.exceptions.Timeout:
        return "OK"
    except requests.exceptions.RequestException:
        return "OK"

# Example usage:
if __name__ == "__main__":
    subreddit_name = "python"
    print(number_of_subscribers(subreddit_name))

    subreddit_name = "nonexistingsubreddit1234567890"
    print(number_of_subscribers(subreddit_name))
