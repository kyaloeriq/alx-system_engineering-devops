#!/usr/bin/python3
"""
Queries the Reddit API, parses the title of all hot articles
"""

from collections import Counter
import requests


def count_words(subreddit, word_list, after=None, word_count=None):
    """
    Queries Reddit API recursively, counts the occurrences of given keywords
    Parameters:
        subreddit (str): The name of the subreddit to query.
        word_list (list): The list of keywords to count.
        after (str): The 'after' parameter for pagination.
        word_count (Counter): Counter to accumulate word occurrences.
    Returns:
        Counter: A Counter object with keyword occurrences if the subreddit
        None: If the subreddit is invalid or no results are found.
    """
    if word_count is None:
        word_count = Counter()

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': (
            'python:subreddit.hot.article.word.counter:v1.0 (by /u/yourusername)'
        )
    }
    params = {'after': after} if after else {}

    try:
        response = requests.get(
                url, headers=headers, params=params, allow_redirects=False
                )
        response.raise_for_status()

        if response.status_code != 200:
            return None

        data = response.json()
        if 'data' not in data:
            return None

        children = data['data']['children']
        if not children:
            return None if not word_count else word_count

        for child in children:
            title = child['data']['title'].lower()
            words = title.split()
            for word in word_list:
                lower_word = word.lower()
                word_count[lower_word] += words.count(lower_word)

        after = data['data'].get('after')
        if after:
            return count_words(subreddit, word_list, after, word_count)
        else:
            return word_count

    except requests.exceptions.HTTPError:
        return None
    except requests.exceptions.ConnectionError:
        return None
    except requests.exceptions.Timeout:
        return None
    except requests.exceptions.RequestException:
        return None


def print_word_counts(word_count):
    """
    Prints the word counts in the specified format.
    Parameters:
        word_count (Counter): A Counter object with keyword occurrences.
    """
    sorted_word_count = sorted(
            word_count.items(), key=lambda item: (-item[1], item[0])
            )
    for word, count in sorted_word_count:
        if count > 0:
            print(f"{word}: {count}")


if __name__ == "__main__":
    subreddit_name = "python"
    keywords = ["Python", "javascript", "java", "C++", "java", "JavaScript"]
    word_count = count_words(subreddit_name, keywords)
    if word_count:
        print_word_counts(word_count)
    else:
        print(f"Subreddit {subreddit_name} is invalid or has no hot articles.")
