#!/usr/bin/python3
"""
Module that contains a function to query the Reddit API
and return the number of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit. If an invalid subreddit is given,
    the function returns 0.

    Args:
        subreddit (str): The name of the subreddit to query

    Returns:
        int: The number of subscribers for the subreddit,
             or 0 if the subreddit is invalid
    """
    # Reddit API URL for getting subreddit info
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    
    # Set custom User-Agent to avoid Too Many Requests errors
    headers = {
        "User-Agent": "linux:reddit_subscriber_counter:v1.0 (by /u/your_username)"
    }
    
    # Make the request
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Return the number of subscribers
        return data.get("data", {}).get("subscribers", 0)
    else:
        # Return 0 for invalid subreddit or other errors
        return 0
