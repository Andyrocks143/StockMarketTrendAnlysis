#! /usr/bin/env python

import tweepy
from auth_info import consumer_key, consumer_secret, access_token, access_token_secret

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print status.text, status.created_at, status.lang


    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            print "420 blaze it"
            return False

def main():

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    myStreamListener = MyStreamListener()

    myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

    myStream.filter(track=['Hitler'], async=True)

if __name__ == "__main__":
    main()
