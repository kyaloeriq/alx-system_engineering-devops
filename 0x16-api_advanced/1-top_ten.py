#!/usr/bin/python3
"""
Queries Reddit API, prints titles of the first 10 hot posts for a subreddit
"""
import requests


def top_ten(subreddit):
    """
    Queries Reddit API, prints titles of the first 10 hot posts for a subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        'User-Agent': (
            'python:subreddit.hot.posts:v1.0 (by /u/yourusername)'
        )
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()

        if response.status_code == 200:
            data = response.json()
            if 'data' in data and 'children' in data['data']:
                posts = data['data']['children']
                for post in posts:
                    print(post['data']['title'])
            else:
                print(None)
        else:
            print(None)
    except requests.exceptions.HTTPError:
        print(None)
    except requests.exceptions.ConnectionError:
        print(None)
    except requests.exceptions.Timeout:
        print(None)
    except requests.exceptions.RequestException:
        print(None)


# Example usage:
if __name__ == "__main__":
    subreddit_name = "python"
    top_ten(subreddit_name)

    subreddit_name = "nonexistingsubreddit1234567890"
    top_ten(subreddit_name)
