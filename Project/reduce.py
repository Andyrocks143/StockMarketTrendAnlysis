#! /usr/bin/env python

#This program parses the dicts that map date to a list of sentiments, and then aggregates them to find date and average sentiment

import pickle
import sys

if len(sys.argv) < 1:
    print "Enter a filename as the cmd line argument"
    exit()

input_file = str(sys.argv[1])
output_file = "red_" + input_file + ".red" 

def average(l):
    return sum(l)/float(len(l))

def parse_file(filename):
    sent_dict = dict()
    with open(filename, 'r') as df:
        sent_dict = pickle.load(df)

    return sent_dict

#Accept a filename as an argument, create a file called red_<filename>.red, which contains date, average positive sentiment, average negative sentiment.

sent_dict = parse_file(input_file)
print sent_dict

red_dict = dict()

for date in sent_dict.keys():
    pos_sent_list = sent_dict[date][0]
    neg_sent_list = sent_dict[date][1]
    pos_avg = average(pos_sent_list)
    neg_avg = average(neg_sent_list)
    red_dict[date] = [pos_avg, neg_avg]

print red_dict

with open(output_file, 'w') as f:
    pickle.dump(red_dict, f)
