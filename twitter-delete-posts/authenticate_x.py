import tweepy

def authenticate_x(api_key, api_secret_key, access_token, access_token_secret):
    auth = tweepy.OAuth1UserHandler(api_key, api_secret_key, access_token, access_token_secret)
    api = tweepy.API(auth)
    return api
