#!/usr/bin/python3
"""
Module that contains a recursive function to query the Reddit API
and return a list of all hot article titles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query
        hot_list (list, optional): List to store the article titles.
                                  Defaults to empty list.
        after (str, optional): Token for pagination. Defaults to None.

    Returns:
        list: List containing all hot article titles or None if invalid subreddit
    """
    # Reddit API URL for getting hot posts
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    
    # Set custom User-Agent to avoid Too Many Requests errors
    headers = {
        "User-Agent": "linux:reddit_all_hot_posts:v1.0 (by /u/your_username)"
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
        
        # Add titles to hot_list
        for post in posts:
            hot_list.append(post.get("data", {}).get("title"))
        
        # If there are more pages, recurse with the after token
        if after_token:
            return recurse(subreddit, hot_list, after_token)
        else:
            return hot_list
    elif response.status_code == 404:
        # Return None for invalid subreddit
        return None
    else:
        # Return current hot_list for other errors
        return hot_list
