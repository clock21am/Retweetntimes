#!usr/bin/python

import tweepy
import twitter
import time

consumer_key = ''
consumer_secret_key = ''
access_key = ''
access_key_secret = ''

auth = tweepy.OAuthHandler(consumer_key,consumer_secret_key);
auth.set_access_token(access_key,access_key_secret);

try:
    redirect_url = auth.get_authorization_url()
except:
    print "failed"


api = tweepy.API(auth);
api.update_status('My first tweet with using tweepy -- a python api twitter');
print api;
