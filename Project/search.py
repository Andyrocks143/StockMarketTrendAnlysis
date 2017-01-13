#! /usr/bin/env python

from TwitterSearch import *

try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['Ebay']) # let's define all words we would like to have a look for
    #tso.set_language('en') 
    tso.set_include_entities(True) 

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = 'h8y6SEbc5UGfw9duzhYFDrfKl',
        consumer_secret = 'oAYKt4OxVgw6x77wPgoS27I0q6XNtbOMp58VKbtfobGxFQakYL',
        access_token = '705107688393461760-FDF4RsfVgdeJ41KEZ8YsWXDOOgyG3Ma',
        access_token_secret = 'dFIDeTI8zRDiXxhEKaWcJv5IfMY8XvMlepGYu6Z3rXfGg'
     )

     # this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):
        print tweet['text']

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print e
