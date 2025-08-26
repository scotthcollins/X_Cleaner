# Instructions to run the script:
# 1. Set your Twitter API credentials as environment variables or pass them as command line arguments.
# 2. Run the script using Python: python delete_tweets.py
# Note: Be cautious as this will permanently delete all your tweets.
# Example using environment variables in Windows PowerShell:
# $env:TWITTER_API_KEY="your_api_key"
# $env:TWITTER_API_SECRET_KEY="your_api_secret_key"
# $env:TWITTER_ACCESS_TOKEN="your_access_token"
# $env:TWITTER_ACCESS_TOKEN_SECRET="your_access_token_secret"
# python delete_tweets.py

# Example using command line arguments:
# python delete_tweets.py 
#   --api-key your_api_key 
#   --api-secret-key your_api_secret_key 
#   --access-token your_access_token 
#   --access-token-secret your_access_token_secret

import os
import sys
import argparse
from authenticate_twitter import authenticate_twitter
from delete_all_tweets import delete_all_tweets


def get_twitter_credentials():
    parser = argparse.ArgumentParser(description="Delete all tweets from your X (Twitter) account.")
    parser.add_argument('--api-key', help='Twitter API Key')
    parser.add_argument('--api-secret-key', help='Twitter API Secret Key')
    parser.add_argument('--access-token', help='Twitter Access Token')
    parser.add_argument('--access-token-secret', help='Twitter Access Token Secret')
    args = parser.parse_args()

    api_key = args.api_key or os.getenv('TWITTER_API_KEY')
    api_secret_key = args.api_secret_key or os.getenv('TWITTER_API_SECRET_KEY')
    access_token = args.access_token or os.getenv('TWITTER_ACCESS_TOKEN')
    access_token_secret = args.access_token_secret or os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

    # Validate that none are null or empty
    if not all([api_key, api_secret_key, access_token, access_token_secret]):
        print("Error: All Twitter API credentials must be provided via environment variables or command line arguments.")
        sys.exit(1)
    return api_key, api_secret_key, access_token, access_token_secret

if __name__ == "__main__":
    API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET = get_twitter_credentials()
    twitter_api = authenticate_twitter(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    delete_all_tweets(twitter_api)

