#!/usr/bin/env python3

import sys
from twitter import *
import config

def get_profile_info(username):
    auth = OAuth(config.access_key,
                 config.access_secret,
                 config.consumer_key,
                 config.consumer_secret)
    twitter = Twitter(auth=auth)

    try:
        user_info = twitter.users.show(screen_name=username)
        print("Name:", user_info["name"])
        print("Screen Name: @", user_info["screen_name"])
        print("Location:", user_info["location"])
        print("Description:", user_info["description"])
    except Exception as e:
        print("Error retrieving user information:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python twitter-profile-info.py <username>")
    else:
        get_profile_info(sys.argv[1])
