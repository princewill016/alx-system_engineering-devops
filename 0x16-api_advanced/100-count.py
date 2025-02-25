#!/usr/bin/python3
"""
Module that contains a recursive function to query the Reddit API,
parse titles of all hot articles, and print a sorted count of given keywords
"""
import requests
import re


def count_words(subreddit, word_list, after=None, word_counts=None):
    """
    Recursively queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit to query
        word_list (list): List of keywords to count
        after (str, optional): Token for pagination. Defaults to None.
        word_counts (dict, optional): Dictionary to track keyword counts.
                                     Defaults to None.
    """
    # Initialize word_counts if this is the first call
    if word_counts is None:
        word_counts = {}
        # Initialize all words in word_list with count 0
        for word in word_list:
            word_counts[word.lower()] = 0
    
    # Reddit API URL for getting hot posts
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    
    # Set custom User-Agent to avoid Too Many Requests errors
    headers = {
        "User-Agent": "linux:reddit_word_counter:v1.0 (by /u/your_username)"
    }
    
    # Parameters for pagination
    params = {
        "limit": 100  # Maximum allowed by Reddit API
    }
    
    # Add 'after' parameter if it exists
    if after:
        params["after"] = after
    
    # Make the request
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        
        # Get pagination token for next page
        after_token = data.get("data", {}).get("after")
        
        # Process titles and count keywords
        for post in posts:
            title = post.get("data", {}).get("title", "").lower()
            # Split the title into words
            words = title.split()
            
            # Count occurrences of each word in word_list
            for word in words:
                # Use regex to match exact word (no partial matches)
                for keyword in word_list:
                    keyword_lower = keyword.lower()
                    # Match only if word is exactly the keyword (no partial matches)
                    if re.match(r'^{}$'.format(word), keyword_lower):
                        word_counts[keyword_lower] += 1
        
        # If there are more pages, recurse with the after token
        if after_token:
            return count_words(subreddit, word_list, after_token, word_counts)
        else:
            # Print results in specified order
            print_results(word_counts)
    elif response.status_code == 404:
        # Invalid subreddit, print nothing
        return
    else:
        # Print current results for other errors
        print_results(word_counts)


def print_results(word_counts):
    """
    Prints the word counts in descending order by count,
    and alphabetically for words with the same count.

    Args:
        word_counts (dict): Dictionary with words and their counts
    """
    # Filter out words with no matches
    filtered_counts = {word: count for word, count in word_counts.items() if count > 0}
    
    # Sort the filtered counts
    sorted_counts = sorted(
        filtered_counts.items(),
        key=lambda x: (-x[1], x[0])  # Sort by count (desc) then word (asc)
    )
    
    # Print the sorted counts
    for word, count in sorted_counts:
        print("{}: {}".format(word, count))
