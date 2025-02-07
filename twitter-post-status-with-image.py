#!/usr/bin/env python3

#-----------------------------------------------------------------------
# twitter-post-status-with-image
#  - posts a tweet with an image using the Twitter API
#-----------------------------------------------------------------------

import tweepy
from config import consumer_key, consumer_secret, access_key, access_secret

def authenticate():
    """Authenticate with the Twitter API using OAuth."""
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    return tweepy.API(auth)

def post_tweet_with_image(message, image_path):
    """Post a tweet with an image."""
    try:
        api = authenticate()
        api.update_with_media(image_path, status=message)
        print("Tweet posted successfully!")
    except Exception as e:
        print(f"Failed to post tweet: {e}")

if __name__ == "__main__":
    message = "Check out this cool image!"
    image_path = "path/to/image.jpg"
    post_tweet_with_image(message, image_path)
