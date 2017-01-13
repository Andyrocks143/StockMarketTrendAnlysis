#! /usr/bin/env python

import os
import os.path
import json
import pickle
from tweet_sentiment_analysis import find_feature_for_tweet

#Find a running average of all the tweets for a particular month

month = 6

#First extract the tar file
    #Then find all the days for which information is present
        #For each day, find all the bz2 files that contain the actual tweets
            #For each bz2 file, extract, find the json file, and then parse the json file and find the running average of the sentiment of all the tweets. 
                #Delete the json files  


tar_file_path = 'data/archiveteam-twitter-stream-2016-0' + str(month) + "/"
extracted_file_path = '2016/0' + str(month) + '/'
classifier_file = "naive_bayes_classifier"
output_file = "ebay_sent_dict"
classifier = None

with open(classifier_file, 'r') as cf:
    classifier = pickle.load(cf)


def find_sentiment(tweet):
    feature_list = find_feature_for_tweet(tweet)
    result = classifier.prob_classify(feature_list)
    return result.prob('positive'), result.prob('negative')

def get_files_by_extension(parent_path, file_extension):
    file_list = list()
    for dirpath, dirnames, filenames in os.walk(parent_path):
        for filename in [f for f in filenames if f.endswith(file_extension)]:
            file_list.append(os.path.join(dirpath, filename))

    return file_list

def extract_tar_file():
    tar_file = get_files_by_extension(tar_file_path, '.tar')[0]
    os.system('tar -xvf ' + tar_file)

def get_date_from_json(json_file):
    file_split = json_file.split('/')
    year = file_split[0]
    month = file_split[1]
    day = file_split[2]
    return year + "-" + month + "-" + day

def average(array):
    return sum(array) / float(len(array))

def parse_bz2(bz2_files):
    #accepts a list of bz2 files, extracts it, gets the tweet from the json file, finds sentiment of the tweet, and then finds the average of positive and negative sentiment, and then deletes the json file 
    counter = 1
    sent_dict = dict()
    for bz2_file in bz2_files:
        os.system("bzip2 -dk " + bz2_file)
        json_file = ('.').join(bz2_file.split('.')[:-1])
        date = get_date_from_json(json_file)
        if date not in sent_dict.keys():
            sent_dict[date] = [[],[]]
        #Find the json file
        with open(json_file, 'r') as jf:
            #parse the json file to find the tweets
            pos_sent_list = list()
            neg_sent_list = list()
            for line in jf:
                tweet_line = json.loads(line)
                #print tweet_line
                if "text" in tweet_line.keys():
                    if (tweet_line['lang'] == 'en' and 'ebay' in tweet_line["text"]): 
                        tweet = tweet_line["text"].encode('UTF-8')
                        pos_sent, neg_sent = find_sentiment(tweet)
                        pos_sent_list.append(pos_sent)
                        neg_sent_list.append(neg_sent)
            sent_dict[date][0] += pos_sent_list
            sent_dict[date][1] += neg_sent_list
        os.system("rm " + json_file)
        with open(output_file, 'w+') as of:
            pickle.dump(sent_dict, of)
        print counter
        counter += 1
    return sent_dict

#extract_tar_file()    
bz2_files = get_files_by_extension(extracted_file_path, '.bz2')

sent_dict = parse_bz2(bz2_files)
print sent_dict
