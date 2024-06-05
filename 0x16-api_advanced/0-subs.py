#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers for a given subreddit
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit
    """
    url = fhttps://www.reddit.com/r/{subreddit}/about.json
    headers = {
        'User-Agent': 'python:subreddit.subscriber.counter:v1.0 (by /u/yourusername)'
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()

        if response.status_code == 200:
            data = response.json()
            if 'data' in data and 'subscribers' in data['data']:
                return data['data']['subscribers']
            else:
                print(f"Error: Unexpected response format for subreddit {subreddit}")
                return 0
        else:
            print(f"Error: Received status code {response.status_code} for subreddit {subreddit}")
            return 0
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # e.g., 404 error
        return 0
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
        return 0
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
        return 0
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")
        return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <subreddit_name>")
        sys.exit(1)

    subreddit_name = sys.argv[1]
    subscribers = number_of_subscribers(subreddit_name)
    print(f"Number of subscribers in r/{subreddit_name}: {subscribers}")
