#!/usr/bin/python3
"""
Queries the Reddit API and returns a list of titles of all hot articles for a given subreddit.
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API recursively and returns a list of titles of all hot articles for a given subreddit.
    
    Parameters:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): The list to accumulate titles of hot articles.
        after (str): The 'after' parameter for pagination.
        
    Returns:
        list: A list of titles of hot articles if the subreddit is valid.
        None: If the subreddit is invalid or no results are found.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': (
            'python:subreddit.hot.article.fetcher:v1.0 (by /u/yourusername)'
        )
    }
    params = {'after': after} if after else {}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        response.raise_for_status()

        # If the status code is not 200, return None
        if response.status_code != 200:
            return None

        data = response.json()
        if 'data' not in data:
            return None

        children = data['data']['children']
        if not children:
            return None if not hot_list else hot_list

        for child in children:
            hot_list.append(child['data']['title'])

        # Check if there is a next page
        after = data['data'].get('after')
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list

    except requests.exceptions.HTTPError:
        return None
    except requests.exceptions.ConnectionError:
        return None
    except requests.exceptions.Timeout:
        return None
    except requests.exceptions.RequestException:
        return None

# Example usage
if __name__ == "__main__":
    subreddit_name = "python"
    hot_titles = recurse(subreddit_name)
    if hot_titles is not None:
        print(f"Titles of hot articles in r/{subreddit_name}:")
        for title in hot_titles:
            print(title)
    else:
        print(f"Subreddit {subreddit_name} is invalid or has no hot articles.")

