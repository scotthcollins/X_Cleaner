import tweepy

def delete_all_tweets(api):
    tweets = api.user_timeline(count=200, tweet_mode='extended')
    while len(tweets) > 0:
        for tweet in tweets:
            try:
                print(f'Deleting tweet ID: {tweet.id} - {tweet.full_text}')
                api.destroy_status(tweet.id)
            except Exception as e:
                print(f'Error deleting tweet ID {tweet.id}: {e}')
        tweets = api.user_timeline(count=200, tweet_mode='extended')