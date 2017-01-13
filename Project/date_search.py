#! /usr/bin/env python

import twitter

def searchTweets(keywords, since_date, to_date):

    api = twitter.Api(
        consumer_key = 'h8y6SEbc5UGfw9duzhYFDrfKl',
        consumer_secret = 'oAYKt4OxVgw6x77wPgoS27I0q6XNtbOMp58VKbtfobGxFQakYL',
        access_token_key = '705107688393461760-FDF4RsfVgdeJ41KEZ8YsWXDOOgyG3Ma',
        access_token_secret = 'dFIDeTI8zRDiXxhEKaWcJv5IfMY8XvMlepGYu6Z3rXfGg')

    query_string = "q={0}%20lang%3Aen%20since%3A{1}%20until%3A{2}%20include%3Aretweets".format('%2C%20OR%20'.join(keywords), since_date, to_date)
    results = api.GetSearch(raw_query = query_string)

    for result in results:
        print result.text.encode('utf-8')
        print result.created_at
        print dir(result)

if __name__ == '__main__':
    searchTweets(['Amazon'], '2016-11-06', '2016-11-10');
