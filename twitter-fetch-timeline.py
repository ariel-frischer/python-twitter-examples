#!/usr/bin/env python3

#-----------------------------------------------------------------------
# twitter-fetch-timeline:
#  - fetches and prints the user timeline for a given Twitter handle
#-----------------------------------------------------------------------

from twitter import *

#-----------------------------------------------------------------------
# load our API credentials 
#-----------------------------------------------------------------------
import sys

sys.path.append(".")
import config

#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
twitter = Twitter(auth=OAuth(config.access_key,
                             config.access_secret,
                             config.consumer_key,
                             config.consumer_secret))

#-----------------------------------------------------------------------
# the Twitter handle whose timeline we want to fetch
#-----------------------------------------------------------------------
username = input("Enter the Twitter handle: ")

#-----------------------------------------------------------------------
# fetch the user timeline
# twitter API docs: https://dev.twitter.com/rest/reference/get/statuses/user_timeline
#-----------------------------------------------------------------------
statuses = twitter.statuses.user_timeline(screen_name=username, count=50)

#-----------------------------------------------------------------------
# loop through each status and print its text
#-----------------------------------------------------------------------
for status in statuses:
    print("(%s) @%s %s" % (status["created_at"], status["user"]["screen_name"], status["text"]))
