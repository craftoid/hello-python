from __future__ import absolute_import, print_function

import tweepy
import sys
from keys import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

print("Tweeting at %s" % api.me().name)

if len(sys.argv) == 1:
	api.update_status(status="I tweet therefor I am!")
else:
	api.update_status(status=" ".join(sys.argv[1:]))
