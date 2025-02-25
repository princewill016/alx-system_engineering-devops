#!/usr/bin/python3
"""
Module that contains a function to query the Reddit API
and print the titles of the first 10 hot posts for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit. If not a valid subreddit, prints None.

    Args:
        subreddit (str): The name of the subreddit to query
    """
    # Reddit API URL for getting hot posts
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    
    # Set custom User-Agent to avoid Too Many Requests errors
    headers = {
        "User-Agent": "linux:reddit_hot_posts:v1.0 (by /u/your_username)"
    }
    
    # Parameters to limit to 10 posts
    params = {
        "limit": 10
    }
    
    # Make the request
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        
        # Print the titles of the first 10 hot posts
        for post in posts:
            print(post.get("data", {}).get("title", ""))
    else:
        # Print None for invalid subreddit
        print(None)
