#! /usr/bin/env python

from sklearn.linear_model import LinearRegression
import numpy as np
import sys
import pickle

if (len(sys.argv) < 2):
    print "Enter a stock name to begin"
    exit()

stock_map = {"ebay": "EBAY", "best": "BBY", "linkedin": "LNKD", "hersheys": "HSY"}

company_name = sys.argv[1]

month = 5

sent_dict_file = "red_" + company_name + "_sent_dict_" + str(month) + '.red'
stock_file_name = 'stock/WIKI-' + stock_map[company_name] + "_dict"

if company_name == "best":
    sent_dict_file = "red_best buy_sent_dict_" + str(month) + '.red'

sent_dict = dict()
stock_dict = dict()

with open(sent_dict_file, 'r') as sf:
    sent_dict = pickle.load(sf)

with open(stock_file_name, 'r') as tf:
    stock_dict = pickle.load(tf)

print sent_dict

training_data_list = list()
training_target_list = list()

for date in sent_dict.keys():
    if date in stock_dict:
        print sent_dict[date]
        training_data_list.append([sent_dict[date][0], sent_dict[date][1]])
        training_target_list.append(stock_dict[date])
    
print training_data_list

X = training_data_list
Y = training_target_list
X = np.asarray(X).reshape(len(X),2)
#Y = np.asarray(Y).reshape(-1,1)

print X, Y

regression_classifier = LinearRegression()
regression_classifier.fit(X, Y)

print regression_classifier.predict([0.1, 0.9])
