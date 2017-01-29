#!usr/bin/python

import tweepy

consumer_key = ''
consumer_secret_key = ''
access_token = ''
access_token_secret = ''

status_retweet = ""

friend_name = ''

auth = tweepy.OAuthHandler(consumer_key,consumer_secret_key);
auth.set_access_token(access_token,access_token_secret);

try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print "lol nothing is working"

api = tweepy.API(auth);

for friend in tweepy.Cursor(api.friends).items():             
    if friend.screen_name == friend_name:
        page = 1
        no_of_tweets = 2
        i = 1
        flag = 0
        while True:
            status = api.user_timeline(screen_name=friend_name,page=page)
            if status:
                for post in status:
                    print post.text 
                    if post.text == status_retweet:
                       print "Yes I have got ur post to retweet"
                       for i in range(no_of_tweets):
                           api.update_status(str(i)+"."+status_retweet,post.id)
                           print "happy"
            else:
                break;
            page+=1
            

          
          
           
