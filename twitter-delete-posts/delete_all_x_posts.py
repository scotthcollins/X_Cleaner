def delete_all_x_posts(api):
import tweepy

def delete_all_x_posts(api):
    posts = api.user_timeline(count=200, tweet_mode='extended')
    while len(posts) > 0:
        for post in posts:
            try:
                print(f'Deleting post ID: {post.id} - {post.full_text}')
                api.destroy_status(post.id)
            except Exception as e:
                print(f'Error deleting post ID {post.id}: {e}')
        posts = api.user_timeline(count=200, tweet_mode='extended')
