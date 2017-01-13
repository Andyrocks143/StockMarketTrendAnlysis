#! /usr/bin/env python

from nltk.corpus import twitter_samples
import json
import csv

print twitter_samples.fileids()

pos_output_file = "pos_tweets_list.txt"
neg_output_file = "neg_tweets_list.txt"

def clean_up_files(filename):
    data = list()
    with open(filename, 'r') as f:
        for line in f:
            if len(line) > 1:
                data.append(line)

    with open(filename, 'w') as f:
        for line in data:
            f.write(line)


pos_tweets_file = twitter_samples.abspath(twitter_samples.fileids()[1])
pos_tweets_output = open(pos_output_file, 'w+')
with open(pos_tweets_file, 'r') as tf:
    for line in tf:
        x = json.loads(line)
        tweet = x['text'].encode('UTF-8')
        if '\n' not in tweet:
            tweet += '\n'
        if (len(tweet) > 4):
            pos_tweets_output.write(tweet)

pos_tweets_output.close() 

neg_tweets_file = twitter_samples.abspath(twitter_samples.fileids()[0])
neg_tweets_output = open(neg_output_file, 'w+')
with open(neg_tweets_file, 'r') as tf:
    for line in tf:
        x = json.loads(line)
        tweet = x['text'].encode('UTF-8')
        #if tweet[-1] != '\n':
        if '\n' not in tweet:
            tweet += '\n'
        if (len(tweet) > 4):
            neg_tweets_output.write(tweet)


neg_tweets_output.close()

clean_up_files(pos_output_file)
clean_up_files(neg_output_file)
